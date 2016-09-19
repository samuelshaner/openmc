module mgxs_header

  use constants,       only: MAX_FILE_LEN, ZERO, ONE, TWO, PI
  use error,           only: fatal_error
  use, intrinsic :: ISO_FORTRAN_ENV,      only: OUTPUT_UNIT
  use list_header,     only: ListInt
  use material_header, only: material
  use math,            only: calc_pn, calc_rn, expand_harmonic, &
                             evaluate_legendre
  use nuclide_header,  only: MaterialMacroXS
  use random_lcg,      only: prn
  use scattdata_header
  use string
  use xml_interface


!===============================================================================
! MGXS contains the base mgxs data for a nuclide/material
!===============================================================================

  type, abstract :: Mgxs
    character(len=104) :: name    ! name of dataset, e.g. 92235.03c
    real(8)            :: awr     ! Atomic Weight Ratio
    real(8)            :: kT      ! temperature in MeV (k*T)

    ! Fission information
    logical :: fissionable   ! mgxs object is fissionable?
    integer :: scatt_type    ! either legendre, histogram, or tabular.

  contains
    procedure(mgxs_init_file_), deferred :: init_file ! Initialize the data
    procedure(mgxs_get_xs_),   deferred  :: get_xs    ! Get the requested xs
    procedure(mgxs_combine_),  deferred  :: combine   ! initializes object

    ! Sample the outgoing energy from a fission event
    procedure(mgxs_sample_fission_), deferred :: sample_fission_energy

    ! Sample the outgoing energy and angle from a scatter event
    procedure(mgxs_sample_scatter_), deferred :: sample_scatter

    ! Calculate the material specific MGXS data from the nuclides
    procedure(mgxs_calculate_xs_), deferred   :: calculate_xs
  end type Mgxs

!===============================================================================
! MGXSCONTAINER pointer array for storing Nuclides
!===============================================================================

  type MgxsContainer
    class(Mgxs), pointer :: obj
  end type MgxsContainer

!===============================================================================
! Interfaces for MGXS
!===============================================================================

  abstract interface
    subroutine mgxs_init_file_(this, node_xsdata, energy_groups, &
         delayed_groups, max_order)

      import Mgxs, Node
      class(Mgxs), intent(inout)      :: this           ! Working Object
      type(Node), pointer, intent(in) :: node_xsdata    ! Data from MGXS xml
      integer, intent(in)             :: energy_groups  ! Number of energy groups
      integer, intent(in)             :: delayed_groups ! Number of delayed groups
      integer, intent(in)             :: max_order      ! Maximum requested order
    end subroutine mgxs_init_file_

    pure function mgxs_get_xs_(this,xstype,gin,gout,uvw,mu,dg) result(xs)

      import Mgxs
      class(Mgxs), intent(in)       :: this
      character(*), intent(in)      :: xstype ! Cross section type
      integer, intent(in)           :: gin    ! Incoming energy group
      integer, optional, intent(in) :: gout   ! Outgoing group
      real(8), optional, intent(in) :: uvw(3) ! Requested angle
      real(8), optional, intent(in) :: mu     ! Change in angle
      integer, optional, intent(in) :: dg      ! Delayed group
      real(8)                       :: xs     ! Resultant xs
    end function mgxs_get_xs_

    pure function mgxs_calc_f_(this,gin,gout,mu,uvw,iazi,ipol,dg) result(f)
      import Mgxs
      class(Mgxs), intent(in)       :: this
      integer, intent(in)           :: gin    ! Incoming energy group
      integer, intent(in)           :: gout   ! Outgoing energy group
      real(8), intent(in)           :: mu     ! Angle of interest
      real(8), intent(in), optional :: uvw(3) ! Direction vector
      integer, intent(in), optional :: iazi   ! Incoming energy group
      integer, intent(in), optional :: ipol   ! Outgoing energy group
      integer, intent(in), optional :: dg     ! Delayed group
      real(8)                       :: f      ! Return value of f(mu)

    end function mgxs_calc_f_

    subroutine mgxs_combine_(this, mat, nuclides, energy_groups, delayed_groups, max_order, scatt_type)
      import Mgxs, Material, MgxsContainer
      class(Mgxs),           intent(inout) :: this          ! The Mgxs to initialize
      type(Material), pointer,  intent(in) :: mat           ! base material
      type(MgxsContainer), intent(in)      :: nuclides(:)   ! List of nuclides to harvest from
      integer, intent(in)                  :: energy_groups ! Number of energy groups
      integer, intent(in)                  :: delayed_groups ! Number of delayed groups
      integer, intent(in)                  :: max_order     ! Maximum requested order
      integer, intent(in)                  :: scatt_type    ! Legendre or Tabular Scatt?
    end subroutine mgxs_combine_

    subroutine mgxs_sample_fission_(this, gin, uvw, dg, gout)
      import Mgxs
      class(Mgxs), intent(in) :: this   ! Data to work with
      integer, intent(in)     :: gin    ! Incoming energy group
      real(8), intent(in)     :: uvw(3) ! Direction vector
      integer, intent(out)    :: dg     ! Delayed group
      integer, intent(out)    :: gout   ! Sampled outgoing group

    end subroutine mgxs_sample_fission_

    subroutine mgxs_sample_scatter_(this, uvw, gin, gout, mu, wgt)
      import Mgxs
      class(Mgxs),    intent(in)    :: this
      real(8),        intent(in)    :: uvw(3) ! Incoming neutron direction
      integer,        intent(in)    :: gin    ! Incoming neutron group
      integer,        intent(out)   :: gout   ! Sampled outgoin group
      real(8),        intent(out)   :: mu     ! Sampled change in angle
      real(8),        intent(inout) :: wgt    ! Particle weight
    end subroutine mgxs_sample_scatter_

    subroutine mgxs_calculate_xs_(this, gin, uvw, xs)
      import Mgxs, MaterialMacroXS
      class(Mgxs),           intent(in)    :: this
      integer,               intent(in)    :: gin    ! Incoming neutron group
      real(8),               intent(in)    :: uvw(3) ! Incoming neutron direction
      type(MaterialMacroXS), intent(inout) :: xs     ! Resultant Mgxs Data
    end subroutine mgxs_calculate_xs_
  end interface

!===============================================================================
! MGXSISO contains the base MGXS data specifically for
! isotropically weighted MGXS
!===============================================================================

  type, extends(Mgxs) :: MgxsIso

    ! Microscopic cross sections
    class(ScattData), allocatable :: scatter        ! Scattering information
    real(8), allocatable :: total(:)                ! Total cross section
    real(8), allocatable :: absorption(:)           ! Absorption cross section
    real(8), allocatable :: delayed_nu_fission(:,:) ! Delayed fission matrix (Gin x Dg)
    real(8), allocatable :: prompt_nu_fission(:)    ! Prompt fission vector (Gin)
    real(8), allocatable :: kappa_fission(:)        ! Kappa-fission
    real(8), allocatable :: fission(:)              ! Neutron production
    real(8), allocatable :: decay_rate(:)           ! Delayed neutron precursor decay rate
    real(8), allocatable :: velocity(:)             ! Neutron velocity
    real(8), allocatable :: chi_delayed(:, :, :)    ! Delayed fission spectra
    real(8), allocatable :: chi_prompt(:, :)        ! Prompt fission spectra

  contains
    procedure :: init_file   => mgxsiso_init_file ! Initialize Nuclidic MGXS Data
    procedure :: get_xs      => mgxsiso_get_xs  ! Gets Size of Data w/in Object
    procedure :: combine     => mgxsiso_combine ! inits object
    procedure :: sample_fission_energy => mgxsiso_sample_fission_energy
    procedure :: sample_scatter => mgxsiso_sample_scatter
    procedure :: calculate_xs => mgxsiso_calculate_xs
  end type MgxsIso

!===============================================================================
! MGXSANGLE contains the base MGXS data specifically for
! angular flux weighted MGXS
!===============================================================================

  type, extends(Mgxs) :: MgxsAngle

    ! Microscopic cross sections
    type(ScattDataContainer), allocatable :: scatter(:, :) ! Scattering information
    real(8), allocatable :: total(:, :, :)                 ! Total cross section
    real(8), allocatable :: absorption(:, :, :)            ! Absorption cross section
    real(8), allocatable :: delayed_nu_fission(:, :, :, :) ! Delayed fission matrix (Gout x Gin)
    real(8), allocatable :: prompt_nu_fission(:, :, :)     ! Prompt fission matrix (Gout x Gin)
    real(8), allocatable :: kappa_fission(:, :, :)         ! Kappa-fission
    real(8), allocatable :: fission(:, :, :)               ! Neutron production
    real(8), allocatable :: decay_rate(:, :, :)            ! Delayed neutron precursor decay rate
    real(8), allocatable :: velocity(:, :, :)              ! Neutron velocity
    real(8), allocatable :: chi_delayed(:, :, :, :, :)     ! Delayed fission spectra
    real(8), allocatable :: chi_prompt(:, :, :, :)         ! Prompt fission spectra

    ! In all cases, right-most indices are theta, phi
    integer              :: n_pol         ! Number of polar angles
    integer              :: n_azi         ! Number of azimuthal angles
    real(8), allocatable :: polar(:)     ! polar angles
    real(8), allocatable :: azimuthal(:) ! azimuthal angles

  contains
    procedure :: init_file   => mgxsang_init_file ! Initialize Nuclidic MGXS Data
    procedure :: get_xs      => mgxsang_get_xs  ! Gets Size of Data w/in Object
    procedure :: combine     => mgxsang_combine ! inits object
    procedure :: sample_fission_energy => mgxsang_sample_fission_energy
    procedure :: sample_scatter => mgxsang_sample_scatter
    procedure :: calculate_xs => mgxsang_calculate_xs
  end type MgxsAngle

  contains

!===============================================================================
! MGXS*_INIT reads in the data from the XML file.  At the point of entry
! the file would have been opened and metadata read.  This routine begins with
! the xsdata object node itself.
!===============================================================================

    subroutine mgxs_init_file(this, node_xsdata)
      class(Mgxs), intent(inout)      :: this        ! Working Object
      type(Node), pointer, intent(in) :: node_xsdata ! Data from MGXS xml

      character(MAX_LINE_LEN) :: temp_str

      ! Load the nuclide metadata
      call get_node_value(node_xsdata, "name", this % name)
      this % name = to_lower(this % name)

      if (check_for_node(node_xsdata, "kT")) then
        call get_node_value(node_xsdata, "kT", this % kT)
      else
        this % kT = ZERO
      end if

      if (check_for_node(node_xsdata, "awr")) then
        call get_node_value(node_xsdata, "awr", this % awr)
      else
        this % awr = -ONE
      end if

      if (check_for_node(node_xsdata, "scatt_type")) then

        call get_node_value(node_xsdata, "scatt_type", temp_str)
        temp_str = trim(to_lower(temp_str))

        if (temp_str == 'legendre') then
          this % scatt_type = ANGLE_LEGENDRE
        else if (temp_str == 'histogram') then
          this % scatt_type = ANGLE_HISTOGRAM
        else if (temp_str == 'tabular') then
          this % scatt_type = ANGLE_TABULAR
        else
          call fatal_error("Invalid scatt_type option!")
        end if

      else
        this % scatt_type = ANGLE_LEGENDRE
      end if

      if (check_for_node(node_xsdata, "fissionable")) then

        call get_node_value(node_xsdata, "fissionable", temp_str)
        temp_str = to_lower(temp_str)

        if (trim(temp_str) == 'true' .or. trim(temp_str) == '1') then
          this % fissionable = .true.
        else
          this % fissionable = .false.
        end if

      else
        call fatal_error("Fissionable element must be set!")
      end if

    end subroutine mgxs_init_file

    subroutine mgxsiso_init_file(this, node_xsdata, energy_groups, &
         delayed_groups, max_order)

      class(MgxsIso), intent(inout)   :: this           ! Working Object
      type(Node), pointer, intent(in) :: node_xsdata    ! Data from MGXS xml
      integer, intent(in)             :: energy_groups  ! Number of energy groups
      integer, intent(in)             :: delayed_groups ! Number of delayed groups
      integer, intent(in)             :: max_order      ! Maximum requested order

      type(Node), pointer     :: node_legendre_mu
      character(MAX_LINE_LEN) :: temp_str
      logical                 :: enable_leg_mu
      real(8), allocatable    :: temp_arr(:), temp_2d(:, :), temp_beta(:)
      real(8), allocatable    :: temp_mult(:, :)
      real(8), allocatable    :: scatt_coeffs(:, :, :)
      real(8), allocatable    :: input_scatt(:, :, :)
      real(8), allocatable    :: temp_scatt(:, :, :)
      real(8)                 :: dmu, mu, norm
      integer                 :: order, order_dim, gin, gout, l, arr_len, dg
      integer                 :: legendre_mu_points, imu

      ! Call generic data gathering routine (will populate the metadata)
      call mgxs_init_file(this, node_xsdata)

      ! Allocate data for all the cross sections
      allocate(this % total(energy_groups))
      allocate(this % absorption(energy_groups))
      allocate(this % delayed_nu_fission(energy_groups, delayed_groups))
      allocate(this % prompt_nu_fission(energy_groups))
      allocate(this % fission(energy_groups))
      allocate(this % kappa_fission(energy_groups))
      allocate(this % decay_rate(delayed_groups))
      allocate(this % velocity(energy_groups))
      allocate(this % chi_delayed(energy_groups, energy_groups, delayed_groups))
      allocate(this % chi_prompt(energy_groups, energy_groups))

      if (this % fissionable) then

        ! There are three options for user input:
        ! 1) chi (v) and nu_fission (v) provided
        !   a) If beta present, prompt_nu_fission = (1 - beta) * nu_fission
        !      and delayed_nu_fission_dg = beta_dg * nu_fission
        !   b) Else, prompt_nu_fission = nu_fission and delayed_nu_fission = 0
        ! 2) nu_fission (m) provided
        !   a) If beta present, prompt_nu_fission = (1 - beta) * nu_fission
        !      and delayed_nu_fission_dg = beta_dg * nu_fission
        !   b) Else, prompt_nu_fission = nu_fission and delayed_nu_fission = 0
        ! 3) chi_prompt (v), chi_delayed (m), nu_fission (v) provided
        !   a) If beta present, prompt_nu_fission = (1 - beta) * nu_fission
        !      and delayed_nu_fission_dg = beta_dg * nu_fission
        !   b) Else, prompt_nu_fission = nu_fission and delayed_nu_fission = 0
        ! 4) chi_prompt (v), chi_delayed (m), prompt_nu_fission (v) and
        !    delayed_nu_fission (v) provided
        !
        ! Based on which option the user has chosen, the chi_prompt,
        ! chi_delayed, prompt_nu_fission, and delayed_nu_fission xs
        ! will be set accordingly.

        ! ----------------------------------------------------------------------
        ! 1) chi (v) and nu_fission (v) provided
        ! ----------------------------------------------------------------------
        if (check_for_node(node_xsdata, "chi")) then

          ! Allocate temporary array for beta
          allocate(temp_beta(delayed_groups))

          ! Set beta
          if (check_for_node(node_xsdata, "beta")) then
            call get_node_array(node_xsdata, "beta", temp_beta)
          else
            temp_beta = ZERO
          end if

          ! Set chi_prompt to chi
          allocate(temp_arr(energy_groups))
          call get_node_array(node_xsdata, "chi", temp_arr)

          do gin = 1, energy_groups
            do gout = 1, energy_groups
              this % chi_prompt(gout, gin) = temp_arr(gout)
            end do

            ! Normalize chi_prompt so its CDF goes to 1
            this % chi_prompt(:, gin) = this % chi_prompt(:, gin) / &
                 sum(this % chi_prompt(:, gin))
          end do

          ! Set chi_delayed to chi_prompt
          do dg = 1, delayed_groups
            this % chi_delayed(:, :, dg) = this % chi_prompt(:, :)
          end do

          ! Deallocate temporary chi array
          deallocate(temp_arr)

          ! Set prompt_nu_fission and delayed_nu_fission using
          ! nu_fission (v) and beta
          if (check_for_node(node_xsdata, "nu_fission")) then

            ! Get nu_fission
            call get_node_array(node_xsdata, "nu_fission", &
                 this % prompt_nu_fission)

            ! ------------------------------------------------------------------
            ! a) If beta present, prompt_nu_fission = (1 - beta) * nu_fission
            !    and delayed_nu_fission_dg = beta_dg * nu_fission
            ! b) Else, prompt_nu_fission = nu_fission and delayed_nu_fission = 0
            ! ------------------------------------------------------------------
            do gin = 1, energy_groups
              do dg = 1, delayed_groups

                ! Set delayed_nu_fission using delayed neutron fraction
                this % delayed_nu_fission(gin, dg) = temp_beta(dg) * &
                     this % prompt_nu_fission(gin)
              end do

              ! Correct prompt_nu_fission using delayed neutron fraction
              this % prompt_nu_fission(gin) = (1 - sum(temp_beta)) * &
                   this % prompt_nu_fission(gin)
            end do

          else
            call fatal_error("If chi provided, nu_fission must be provided")
          end if

          ! Deallocate temporary beta array
          deallocate(temp_beta)

          ! --------------------------------------------------------------------
          ! 2) nu_fission (m) provided
          ! --------------------------------------------------------------------
        else if (check_for_node(node_xsdata, "nu_fission") .and. .not. &
             (check_for_node(node_xsdata, "chi_prompt") .or. &
             check_for_node(node_xsdata, "chi_delayed"))) then

          ! Allocate temporary array for beta
          allocate(temp_beta(delayed_groups))

          ! Set beta
          if (check_for_node(node_xsdata, "beta")) then
            call get_node_array(node_xsdata, "beta", temp_beta)
          else
            temp_beta = ZERO
          end if

          ! chi is embedded in nu_fission -> extract chi
          allocate(temp_arr(energy_groups * energy_groups))
          call get_node_array(node_xsdata, "nu_fission", temp_arr)
          allocate(temp_2d(energy_groups, energy_groups))
          temp_2d = reshape(temp_arr, (/energy_groups, energy_groups/))

          ! Deallocate temporary 1D array for nu_fission matrix
          deallocate(temp_arr)

          ! Set the vector nu-fission from the matrix nu-fission
          do gin = 1, energy_groups
            this % prompt_nu_fission(gin) = sum(temp_2d(:, gin))
          end do

          ! --------------------------------------------------------------------
          ! a) If beta present, prompt_nu_fission = (1 - beta) * nu_fission
          !    and delayed_nu_fission_dg = beta_dg * nu_fission
          ! b) Else, prompt_nu_fission = nu_fission and delayed_nu_fission = 0
          ! --------------------------------------------------------------------
          do gin = 1, energy_groups
            do dg = 1, delayed_groups

              ! Set delayed_nu_fission using delayed neutron fraction
              this % delayed_nu_fission(gin, dg) = temp_beta(dg) * &
                   this % prompt_nu_fission(gin)
            end do

            ! Correct prompt_nu_fission using delayed neutron fraction
            this % prompt_nu_fission(gin) = (1 - sum(temp_beta)) * &
                 this % prompt_nu_fission(gin)
          end do

          ! Deallocate temporary beta array
          deallocate(temp_beta)

          ! Now pull out information needed for chi
          this % chi_prompt(:, :) = temp_2d

          ! Deallocate temporary 2D array for nu_fission matrix
          deallocate(temp_2d)

          ! Normalize chi so its CDF goes to 1
          do gin = 1, energy_groups
            this % chi_prompt(:, gin) = this % chi_prompt(:, gin) / &
                 sum(this % chi_prompt(:, gin))
          end do

          ! Set chi_delayed to chi_prompt
          do dg = 1, delayed_groups
            this % chi_delayed(:, :, dg) = this % chi_prompt(:, :)
          end do

          ! --------------------------------------------------------------------
          ! 3) chi_prompt (v), chi_delayed (m), nu_fission (v) provided
          ! --------------------------------------------------------------------
        else if (.not. check_for_node(node_xsdata, "delayed_nu_fission")) then

          ! Allocate temporary array for beta
          allocate(temp_beta(delayed_groups))

          ! Set beta
          if (check_for_node(node_xsdata, "beta")) then
            call get_node_array(node_xsdata, "beta", temp_beta)
          else
            temp_beta = ZERO
          end if

          ! Set chi_prompt
          if (check_for_node(node_xsdata, "chi_prompt")) then

            ! Allocate temporary array for chi_prompt
            allocate(temp_arr(energy_groups))

            ! Get array with chi_prompt
            call get_node_array(node_xsdata, "chi_prompt", temp_arr)

            do gin = 1, energy_groups
              do gout = 1, energy_groups
                this % chi_prompt(gout, gin) = temp_arr(gout)
              end do

              ! Normalize chi so its CDF goes to 1
              this % chi_prompt(:, gin) = this % chi_prompt(:, gin) / &
                   sum(this % chi_prompt(:, gin))
            end do

            ! Deallocate temporary array for chi_prompt
            deallocate(temp_arr)

          else
            call fatal_error("If chi and nu_fission not provided, chi_prompt &
                 &must be provided")
          end if

          ! Set chi_delayed
          if (check_for_node(node_xsdata, "chi_delayed")) then

            ! Allocate temporary array for chi_delayed
            allocate(temp_arr(energy_groups * delayed_groups))

            ! Get array with chi_delayed
            call get_node_array(node_xsdata, "chi_delayed", temp_arr)
            allocate(temp_2d(energy_groups, energy_groups))
            temp_2d = reshape(temp_arr, (/energy_groups, delayed_groups/))

            do dg = 1, delayed_groups
              do gin = 1, energy_groups
                do gout = 1, energy_groups
                  this % chi_delayed(gout, gin, dg) = temp_2d(gout, dg)
                end do

                ! Normalize chi so its CDF goes to 1
                this % chi_delayed(:, gin, dg) = &
                     this % chi_delayed(:, gin, dg) / &
                     sum(this % chi_delayed(:, gin, dg))
              end do
            end do

            ! Deallocate temporary arrays for chi_delayed
            deallocate(temp_arr)
            deallocate(temp_2d)

          else
            call fatal_error("If chi and nu_fision not provided, chi_delayed &
                 &must be provided")
          end if

          ! Set prompt_nu_fission and delayed_nu_fission using
          ! nu_fission (v) and beta
          if (check_for_node(node_xsdata, "nu_fission")) then

            ! Get nu_fission
            call get_node_array(node_xsdata, "nu_fission", &
                 this % prompt_nu_fission)

            ! ------------------------------------------------------------------
            ! a) If beta present, prompt_nu_fission = (1 - beta) * nu_fission
            !    and delayed_nu_fission_dg = beta_dg * nu_fission
            ! b) Else, prompt_nu_fission = nu_fission and delayed_nu_fission = 0
            ! ------------------------------------------------------------------
            do gin = 1, energy_groups
              do dg = 1, delayed_groups

                ! Set delayed_nu_fission using delayed neutron fraction
                this % delayed_nu_fission(gin, dg) = temp_beta(dg) * &
                     this % prompt_nu_fission(gin)
              end do

              ! Correct prompt_nu_fission using delayed neutron fraction
              this % prompt_nu_fission(gin) = (1 - sum(temp_beta)) * &
                   this % prompt_nu_fission(gin)
            end do

          else
            call fatal_error("If chi provided, nu_fission must be provided")
          end if

          ! Deallocate temporary beta array
          deallocate(temp_beta)

          ! --------------------------------------------------------------------
          ! 4) chi_prompt (v), chi_delayed (m), prompt_nu_fission (v)
          !    and delayed_nu_fission (v) provided
          ! --------------------------------------------------------------------
        else

          ! Set chi_prompt
          if (check_for_node(node_xsdata, "chi_prompt")) then

            ! Allocate temporary array for chi_prompt
            allocate(temp_arr(energy_groups))

            ! Get array with chi_prompt
            call get_node_array(node_xsdata, "chi_prompt", temp_arr)

            do gin = 1, energy_groups
              do gout = 1, energy_groups
                this % chi_prompt(gout, gin) = temp_arr(gout)
              end do

              ! Normalize chi so its CDF goes to 1
              this % chi_prompt(:, gin) = this % chi_prompt(:, gin) / &
                   sum(this % chi_prompt(:, gin))
            end do

            ! Deallocate temporary array for chi_prompt
            deallocate(temp_arr)

          else
            call fatal_error("If chi and nu_fission not provided, chi_prompt &
                 &must be provided")
          end if

          ! Set prompt_nu_fission
          if (check_for_node(node_xsdata, "prompt_nu_fission")) then
            call get_node_array(node_xsdata, "prompt_nu_fission", this % prompt_nu_fission)
          else
            call fatal_error("If chi and nu_fission not provided, &
                 &prompt_nu_fission must be provided")
          end if

          ! Set chi_delayed
          if (check_for_node(node_xsdata, "chi_delayed")) then

            ! Allocate temporary array for chi_delayed
            allocate(temp_arr(energy_groups * delayed_groups))

            ! Get array with chi_delayed
            call get_node_array(node_xsdata, "chi_delayed", temp_arr)
            allocate(temp_2d(energy_groups, energy_groups))
            temp_2d = reshape(temp_arr, (/energy_groups, delayed_groups/))

            do gin = 1, energy_groups
              do gout = 1, energy_groups
                do dg = 1, delayed_groups
                  this % chi_delayed(gout, gin, dg) = temp_2d(gout, dg)
                end do
              end do

              ! Normalize chi so its CDF goes to 1
              do dg = 1, delayed_groups
                this % chi_delayed(:, gin, dg) = &
                     this % chi_delayed(:, gin, dg) / &
                     sum(this % chi_delayed(:, gin, dg))
              end do
            end do

            ! Deallocate temporary arrays for chi_delayed
            deallocate(temp_arr)
            deallocate(temp_2d)

          else
            call fatal_error("If chi and nu_fision not provided, chi_delayed &
                 &must be provided")
          end if

          ! Set delayed_nu_fission
          if (check_for_node(node_xsdata, "delayed_nu_fission")) then

            ! Allocate temporary array for delayed_nu_fission
            allocate(temp_arr(energy_groups * delayed_groups))

            ! Get array with delayed_nu_fission
            call get_node_array(node_xsdata, "delayed_nu_fission", temp_arr)

            this % delayed_nu_fission(:, :) = &
                 reshape(temp_arr, (/energy_groups, delayed_groups/))

            ! Deallocate temporary array for delayed_nu_fission
            deallocate(temp_arr)

          else
            call fatal_error("If chi and nu_fission not provided, &
                 &delayed_nu_fission must be provided")
          end if
        end if

        ! chi_prompt, chi_delayed, prompt_nu_fission, and delayed_nu_fission
        ! have been set; Now we will check for the rest of the XS that are
        ! unique to fissionable isotopes

        ! Get fission xs
        if (check_for_node(node_xsdata, "fission")) then
          call get_node_array(node_xsdata, "fission", this % fission)
        else
          this % fission = ZERO
        end if

        ! Get kappa_fission xs
        if (check_for_node(node_xsdata, "kappa_fission")) then
          call get_node_array(node_xsdata, "kappa_fission", this % kappa_fission)
        else
          this % kappa_fission = ZERO
        end if

        ! Get decay rate xs
        if (check_for_node(node_xsdata, "decay_rate")) then
          call get_node_array(node_xsdata, "decay_rate", this % decay_rate)
        else
          this % decay_rate = ZERO
        end if
      else
        this % delayed_nu_fission = ZERO
        this % prompt_nu_fission  = ZERO
        this % fission            = ZERO
        this % kappa_fission      = ZERO
        this % chi_delayed        = ZERO
        this % chi_prompt         = ZERO
        this % decay_rate         = ZERO
      end if

      ! All the XS unique to fissionable isotopes have been set; Now set all
      ! the generation XS

      ! Get absorption xs
      if (check_for_node(node_xsdata, "absorption")) then
        call get_node_array(node_xsdata, "absorption", this % absorption)
      else
        call fatal_error("Must provide absorption!")
      end if

      ! Get velocity
      if (check_for_node(node_xsdata, "velocity")) then
        call get_node_array(node_xsdata, "velocity", this % velocity)
      else
        this % velocity = ZERO
      end if

      ! Allocate temporary 2D array for multiplicity matrix
      allocate(temp_mult(energy_groups, energy_groups))

      ! Get multiplication data if present
      if (check_for_node(node_xsdata, "multiplicity")) then

        arr_len = get_arraysize_double(node_xsdata, "multiplicity")

        if (arr_len == energy_groups * energy_groups) then

          ! Allocate temporary 1D array for multiplicity matrix
          allocate(temp_arr(arr_len))

          ! Get multiplcity matrix and convert to 2D array
          call get_node_array(node_xsdata, "multiplicity", temp_arr)
          temp_mult(:, :) = reshape(temp_arr, (/energy_groups, energy_groups/))

          ! Deallocate temporary 1D array for multiplicity matrix
          deallocate(temp_arr)

        else
          call fatal_error("Multiplicity length be the same as number of &
               &groups squared!")
        end if

      else
        temp_mult(:, :) = ONE
      end if

      ! Get scattering treatment information
      ! Tabular_legendre tells us if we are to treat the provided
      ! Legendre polynomials as tabular data (if enable is true, default)
      ! or leaving them as Legendres (if enable is false)

      ! Set the default (Convert to tabular format w/ 33 points)
      enable_leg_mu = .true.
      legendre_mu_points = 33

      ! Get the user-provided values
      if (check_for_node(node_xsdata, "tabular_legendre")) then

        call get_node_ptr(node_xsdata, "tabular_legendre", node_legendre_mu)

        if (check_for_node(node_legendre_mu, "enable")) then

          call get_node_value(node_legendre_mu, "enable", temp_str)
          temp_str = trim(to_lower(temp_str))

          if (temp_str == 'true' .or. temp_str == '1') then
            enable_leg_mu = .true.
          elseif (temp_str == 'false' .or. temp_str == '0') then
            enable_leg_mu = .false.
          else
            call fatal_error("Unrecognized tabular_legendre/enable: " &
                 // temp_str)
          end if
        end if

        ! Ok, so if we need to convert to a tabular form, get the user provided
        ! number of points
        if (enable_leg_mu) then
          if (check_for_node(node_legendre_mu, "num_points")) then

            call get_node_value(node_legendre_mu, "num_points", &
                 legendre_mu_points)

            if (legendre_mu_points <= 0) &
                 call fatal_error("num_points element must be positive&
                                  & and non-zero!")
          else

            ! Set the default number of points (0.0625 spacing)
            legendre_mu_points = 33
          end if
        end if
      end if

      ! Get the library's value for the order
      if (check_for_node(node_xsdata, "order")) then
        call get_node_value(node_xsdata, "order", order)
      else
        call fatal_error("Order must be provided!")
      end if

      ! Before retrieving the data, store the dimensionality of the data in
      ! order_dim.  For Legendre data, we usually refer to it as Pn where
      ! n is the order.  However Pn has n+1 sets of points (since you need to
      ! the count the P0 moment).  Adjust for that.  Histogram and Tabular
      ! formats dont need this adjustment.
      if (this % scatt_type == ANGLE_LEGENDRE) then
        order_dim = order + 1
      else
        order_dim = order
      end if

      ! The input is gathered in the more user-friendly facing format of
      ! Gout x Gin x Order.  We will get it in that format in input_scatt,
      ! but then need to convert it to a more useful ordering for processing
      ! (Order x Gout x Gin).
      allocate(input_scatt(energy_groups, energy_groups, order_dim))

      if (check_for_node(node_xsdata, "scatter")) then

        allocate(temp_arr(energy_groups * energy_groups * order_dim))
        call get_node_array(node_xsdata, "scatter", temp_arr)
        input_scatt = reshape(temp_arr, (/energy_groups, energy_groups, order_dim/))
        deallocate(temp_arr)

        ! Compare the number of orders given with the maximum order of the
        ! problem.  Strip off the supefluous orders if needed.
        if (this % scatt_type == ANGLE_LEGENDRE) then
          order = min(order_dim - 1, max_order)
          order_dim = order + 1
        end if

        allocate(temp_scatt(energy_groups, energy_groups, order_dim))
        temp_scatt(:, :, :) = input_scatt(:, :, 1:order_dim)

        ! Take input format (groups, groups, order) and convert to
        ! the more useful format needed for scattdata: (order, groups, groups)
        ! However, if scatt_type was ANGLE_LEGENDRE (i.e., the data was
        ! provided as Legendre coefficients), and the user requested that
        ! these legendres be converted to tabular form (note this is also
        ! the default behavior), convert that now.
        if (this % scatt_type == ANGLE_LEGENDRE .and. enable_leg_mu) then

          ! Convert input parameters to what we need for the rest.
          this % scatt_type = ANGLE_TABULAR
          order_dim = legendre_mu_points
          order = order_dim
          dmu = TWO / real(order - 1, 8)

          allocate(scatt_coeffs(order_dim, energy_groups, energy_groups))

          do gin = 1, energy_groups
            do gout = 1, energy_groups
              norm = ZERO
              do imu = 1, order_dim
                if (imu == 1) then
                  mu = -ONE
                else if (imu == order_dim) then
                  mu = ONE
                else
                  mu = -ONE + real(imu - 1, 8) * dmu
                end if

                scatt_coeffs(imu, gout, gin) = &
                     evaluate_legendre(temp_scatt(gout, gin, :),mu)

                ! Ensure positivity of distribution
                if (scatt_coeffs(imu, gout, gin) < ZERO) &
                     scatt_coeffs(imu, gout, gin) = ZERO

                ! And accrue the integral
                if (imu > 1) then
                  norm = norm + HALF * dmu * &
                       (scatt_coeffs(imu - 1, gout, gin) + &
                        scatt_coeffs(imu, gout, gin))
                end if
              end do

              ! Now that we have the integral, lets ensure that the distribution
              ! is normalized such that it preserves the original scattering xs
              if (norm > ZERO) then
                scatt_coeffs(:, gout, gin) = scatt_coeffs(:, gout, gin) * &
                     temp_scatt(gout, gin, 1) / norm
              end if
            end do
          end do
        else

          ! Sticking with current representation, carry forward but change
          ! the array ordering
          allocate(scatt_coeffs(order_dim, energy_groups, energy_groups))

          do gin = 1, energy_groups
            do gout = 1, energy_groups
              do l = 1, order_dim
                scatt_coeffs(l, gout, gin) = temp_scatt(gout, gin, l)
              end do
            end do
          end do
        end if
        deallocate(temp_scatt)
      else
        call fatal_error("Must provide scatter!")
      end if

      ! Allocate and initialize our ScattData Object.
      if (this % scatt_type == ANGLE_HISTOGRAM) then
        allocate(ScattDataHistogram :: this % scatter)
      else if (this % scatt_type == ANGLE_TABULAR) then
        allocate(ScattDataTabular :: this % scatter)
      else if (this % scatt_type == ANGLE_LEGENDRE) then
        allocate(ScattDataLegendre :: this % scatter)
      end if

      ! Initialize the ScattData Object
      call this % scatter % init(temp_mult, scatt_coeffs)

      ! Check absorption xs to ensure it is not 0 since it is
      ! often divided by in the tally routines
      ! (This may happen with Helium data)
      do gin = 1, energy_groups
        if (this % absorption(gin) == ZERO) this % absorption(gin) = 1E-10_8
      end do

      ! Get or infer total xs data.
      if (check_for_node(node_xsdata, "total")) then
        call get_node_array(node_xsdata, "total", this % total)
      else
        this % total(:) = this % absorption(:) + this % scatter % scattxs(:)
      end if

      ! Deallocate temporaries for the next material
      deallocate(input_scatt, scatt_coeffs, temp_mult)

      ! Finally, check total xs to ensure it is not 0 since it is
      ! often divided by in the tally routines
      do gin = 1, energy_groups
        if (this % total(gin) == ZERO) this % total(gin) = 1E-10_8
      end do

    end subroutine mgxsiso_init_file

    subroutine mgxsang_init_file(this, node_xsdata, energy_groups, &
         delayed_groups, max_order)

      class(MgxsAngle), intent(inout) :: this           ! Working Object
      type(Node), pointer, intent(in) :: node_xsdata    ! Data from MGXS xml
      integer, intent(in)             :: energy_groups  ! Energy groups
      integer, intent(in)             :: delayed_groups ! Delayed groups
      integer, intent(in)             :: max_order      ! Max requested order

      type(Node), pointer     :: node_legendre_mu
      character(MAX_LINE_LEN) :: temp_str
      logical                 :: enable_leg_mu
      real(8), allocatable    :: temp_arr(:), temp_4d(:, :, :, :)
      real(8), allocatable    :: temp_beta(:), temp_beta_3d(:, :, :)
      real(8), allocatable    :: temp_mult(:, :, :, :)
      real(8), allocatable    :: scatt_coeffs(:, :, :, :, :)
      real(8), allocatable    :: input_scatt(:, :, :, :, :)
      real(8), allocatable    :: temp_scatt(:, :, :, :, :)
      real(8)                 :: dmu, mu, norm, dangle
      integer                 :: order, order_dim, gin, gout, l, arr_len, dg
      integer                 :: legendre_mu_points, imu, ipol, iazi

      ! Call generic data gathering routine (will populate the metadata)
      call mgxs_init_file(this, node_xsdata)

      if (check_for_node(node_xsdata, "num_polar")) then
        call get_node_value(node_xsdata, "num_polar", this % n_pol)
      else
        call fatal_error("num_polar must be provided!")
      end if

      if (check_for_node(node_xsdata, "num_azimuthal")) then
        call get_node_value(node_xsdata, "num_azimuthal", this % n_azi)
      else
        call fatal_error("num_azimuthal must be provided!")
      end if

      ! Load angle data, if present (else equally spaced)
      allocate(this % polar(this % n_pol))
      allocate(this % azimuthal(this % n_azi))

      if (check_for_node(node_xsdata, "polar")) then

        call fatal_error("User-Specified polar angle bins not yet supported!")

        ! When this feature is supported, this line will be activated
        call get_node_array(node_xsdata, "polar", this % polar)
      else

        dangle = PI / real(this % n_pol, 8)

        do ipol = 1, this % n_pol
          this % polar(ipol) = (real(ipol, 8) - HALF) * dangle
        end do
      end if

      if (check_for_node(node_xsdata, "azimuthal")) then

        call fatal_error("User-Specified azimuthal angle bins not yet supported!")

        ! When this feature is supported, this line will be activated
        call get_node_array(node_xsdata, "azimuthal", this % azimuthal)

      else

        dangle = TWO * PI / real(this % n_azi, 8)

        do iazi = 1, this % n_azi
          this % azimuthal(iazi) = -PI + (real(iazi, 8) - HALF) * dangle
        end do
      end if

      ! Load the more specific data
      allocate(this % prompt_nu_fission(energy_groups, this % n_azi, &
           this % n_pol))
      allocate(this % delayed_nu_fission(energy_groups, &
           this % n_azi, this % n_pol, delayed_groups))
      allocate(this % chi_prompt(energy_groups, energy_groups, this % n_azi, &
           this % n_pol))
      allocate(this % chi_delayed(energy_groups, energy_groups, this % n_azi, &
           this % n_pol, delayed_groups))
      allocate(this % total(energy_groups, this % n_azi, this % n_pol))
      allocate(this % absorption(energy_groups, this % n_azi, this % n_pol))
      allocate(this % fission(energy_groups, this % n_azi, this % n_pol))
      allocate(this % kappa_fission(energy_groups, this % n_azi, this % n_pol))
      allocate(this % decay_rate(this % n_azi, this % n_pol, delayed_groups))
      allocate(this % velocity(energy_groups, this % n_azi, this % n_pol))

      if (this % fissionable) then

        ! There are three options for user input:
        ! 1) chi (v) and nu_fission (v) provided
        !   a) If beta present, prompt_nu_fission = (1 - beta) * nu_fission
        !      and delayed_nu_fission_dg = beta_dg * nu_fission
        !   b) Else, prompt_nu_fission = nu_fission and delayed_nu_fission = 0
        ! 2) nu_fission (m) provided
        !   a) If beta present, prompt_nu_fission = (1 - beta) * nu_fission
        !      and delayed_nu_fission_dg = beta_dg * nu_fission
        !   b) Else, prompt_nu_fission = nu_fission and delayed_nu_fission = 0
        ! 3) chi_prompt (v), chi_delayed (m), nu_fission (v) provided
        !   a) If beta present, prompt_nu_fission = (1 - beta) * nu_fission
        !      and delayed_nu_fission_dg = beta_dg * nu_fission
        !   b) Else, prompt_nu_fission = nu_fission and delayed_nu_fission = 0
        ! 4) chi_prompt (v), chi_delayed (m), prompt_nu_fission (v)
        !    and delayed_nu_fission (v) provided
        !
        ! Based on which option the user has chosen, the chi_prompt,
        ! chi_delayed, prompt_nu_fission, and delayed_nu_fission xs
        ! will be set accordingly.

        ! ----------------------------------------------------------------------
        ! 1) chi (v) and nu_fission (v) provided
        ! ----------------------------------------------------------------------
        if (check_for_node(node_xsdata, "chi")) then

          ! Allocate temporary arrays for beta
          allocate(temp_beta(this % n_azi * this % n_pol * delayed_groups))
          allocate(temp_beta_3d(this % n_azi, this % n_pol, delayed_groups))

          ! Set beta
          if (check_for_node(node_xsdata, "beta")) then
            call get_node_array(node_xsdata, "beta", temp_beta)
          else
            temp_beta = ZERO
          end if

          ! Reshape beta array
          temp_beta_3d(:, :, :) = reshape(temp_beta, &
               (/this % n_azi, this % n_pol, delayed_groups/))

          ! Set chi_prompt to chi
          allocate(temp_arr(1 * energy_groups * this % n_azi * this % n_pol))
          call get_node_array(node_xsdata, "chi", temp_arr)

          ! Initialize counter for temp_arr
          l = 0
          gin = 1
          do ipol = 1, this % n_pol
            do iazi = 1, this % n_azi
              do gout = 1, energy_groups
                l = l + 1
                this % chi_prompt(gout, gin, iazi, ipol) = temp_arr(l)
              end do

              ! Normalize chi so its CDF goes to 1
              this % chi_prompt(:, gin, iazi, ipol) = &
                   this % chi_prompt(:, gin, iazi, ipol) / &
                   sum(this % chi_prompt(:, gin, iazi, ipol))
            end do
          end do

          ! Now set all the other gin values
          do ipol = 1, this % n_pol
            do iazi = 1, this % n_azi
              do gin = 2, energy_groups
                this % chi_prompt(:, gin, iazi, ipol) = &
                     this % chi_prompt(:, 1, iazi, ipol)
              end do
            end do
          end do

          ! Set chi_delayed to chi_prompt
          do dg = 1, delayed_groups
            this % chi_delayed(:, :, :, :, dg) = this % chi_prompt(:, :, :, :)
          end do

          ! Deallocate temporary chi array
          deallocate(temp_arr)

          ! Get nu_fission (as a vector)
          if (check_for_node(node_xsdata, "nu_fission")) then

            ! Allocate temporary array for nu_fission
            allocate(temp_arr(energy_groups * this % n_azi * this % n_pol))

            ! Get nu_fission
            call get_node_array(node_xsdata, "nu_fission", temp_arr)
            this % prompt_nu_fission(:, :, :) = reshape(temp_arr, &
                 (/energy_groups, this % n_azi, this % n_pol/))

            ! Deallocate temporary array for nu_fission
            deallocate(temp_arr)

            ! ------------------------------------------------------------------
            ! a) If beta present, prompt_nu_fission = (1 - beta) * nu_fission
            !    and delayed_nu_fission_dg = beta_dg * nu_fission
            ! b) Else, prompt_nu_fission = nu_fission and delayed_nu_fission = 0
            ! ------------------------------------------------------------------
            do gin = 1, energy_groups
              do ipol = 1, this % n_pol
                do iazi = 1, this % n_azi
                  do dg = 1, delayed_groups

                    ! Set delayed_nu_fission using delayed neutron fraction
                    this % delayed_nu_fission(gin, iazi, ipol, dg) = &
                         temp_beta_3d(iazi, ipol, dg) * &
                         this % prompt_nu_fission(gin, iazi, ipol)
                  end do

                  ! Correct prompt_nu_fission using delayed neutron fraction
                  this % prompt_nu_fission(gin, iazi, ipol) = &
                       (1 - sum(temp_beta_3d(iazi, ipol, :))) * &
                       this % prompt_nu_fission(gin, iazi, ipol)
                end do
              end do
            end do
          else
            call fatal_error("If chi provided, nu_fission must be provided")
          end if

          ! Deallocate temporary beta arrays
          deallocate(temp_beta)
          deallocate(temp_beta_3d)

          ! --------------------------------------------------------------------
          ! 2) nu_fission (m) provided
          ! --------------------------------------------------------------------
        else if (check_for_node(node_xsdata, "nu_fission")) then

          ! Allocate temporary arrays for beta
          allocate(temp_beta(this % n_azi * this % n_pol * delayed_groups))
          allocate(temp_beta_3d(this % n_azi, this % n_pol, delayed_groups))

          ! Set beta
          if (check_for_node(node_xsdata, "beta")) then
            call get_node_array(node_xsdata, "beta", temp_beta)
          else
            temp_beta = ZERO
          end if

          ! Reshape beta array
          temp_beta_3d(:, :, :) = reshape(temp_beta, &
               (/this % n_azi, this % n_pol, delayed_groups/))

          ! Allocate temporary arrays for nu_fission matrix
          allocate(temp_arr(energy_groups * energy_groups * this % n_azi * &
               this % n_pol))
          allocate(temp_4d(energy_groups, energy_groups, this % n_azi, &
               this % n_pol))

          ! chi is embedded in nu_fission -> extract chi
          call get_node_array(node_xsdata, "nu_fission", temp_arr)
          temp_4d(:, :, :, :) = reshape(temp_arr, (/energy_groups, &
               energy_groups, this % n_azi, this % n_pol/))

          ! Deallocate temporary 1D array for nu_fission matrix
          deallocate(temp_arr)

          ! Set the vector nu-fission from the matrix nu-fission
          do ipol = 1, this % n_pol
            do iazi = 1, this % n_azi
              do gin = 1, energy_groups
                this % prompt_nu_fission(gin, iazi, ipol) = &
                     sum(temp_4d(:, gin, iazi, ipol))
              end do
            end do
          end do

          ! Now pull out information needed for chi
          this % chi_prompt = temp_4d

          ! Normalize chi so its CDF goes to 1
          do ipol = 1, this % n_pol
            do iazi = 1, this % n_azi
              do gin = 1, energy_groups
                this % chi_prompt(:, gin, iazi, ipol) = &
                     this % chi_prompt(:, gin, iazi, ipol) / &
                     sum(this % chi_prompt(:, gin, iazi, ipol))
              end do
            end do
          end do

          ! Set chi_delayed to chi_prompt
          do dg = 1, delayed_groups
            this % chi_delayed(:, :, :, :, dg) = this % chi_prompt(:, :, :, :)
          end do

          ! Deallocate temporary chi array
          deallocate(temp_4d)

          ! ------------------------------------------------------------------
          ! a) If beta present, prompt_nu_fission = (1 - beta) * nu_fission
          !    and delayed_nu_fission_dg = beta_dg * nu_fission
          ! b) Else, prompt_nu_fission = nu_fission and delayed_nu_fission = 0
          ! ------------------------------------------------------------------
          do gin = 1, energy_groups
            do ipol = 1, this % n_pol
              do iazi = 1, this % n_azi
                do dg = 1, delayed_groups

                  ! Set delayed_nu_fission using delayed neutron fraction
                  this % delayed_nu_fission(gin, iazi, ipol, dg) = &
                       temp_beta_3d(iazi, ipol, dg) * &
                       this % prompt_nu_fission(gin, iazi, ipol)
                end do

                ! Correct prompt_nu_fission using delayed neutron fraction
                this % prompt_nu_fission(gin, iazi, ipol) = &
                     (1 - sum(temp_beta_3d(iazi, ipol, :))) * &
                     this % prompt_nu_fission(gin, iazi, ipol)
              end do
            end do
          end do

          ! Deallocate temporary beta arrays
          deallocate(temp_beta)
          deallocate(temp_beta_3d)

          ! --------------------------------------------------------------------
          ! 3) chi_prompt (v), chi_delayed (m), nu_fission (v) provided
          ! --------------------------------------------------------------------
        else if (.not. check_for_node(node_xsdata, "delayed_nu_fission")) then

          ! Allocate temporary arrays for beta
          allocate(temp_beta(this % n_azi * this % n_pol * delayed_groups))
          allocate(temp_beta_3d(this % n_azi, this % n_pol, delayed_groups))

          ! Set beta
          if (check_for_node(node_xsdata, "beta")) then
            call get_node_array(node_xsdata, "beta", temp_beta)
          else
            temp_beta = ZERO
          end if

          ! Reshape beta array
          temp_beta_3d(:, :, :) = reshape(temp_beta, &
               (/this % n_azi, this % n_pol, delayed_groups/))

          ! Set chi_prompt
          if (check_for_node(node_xsdata, "chi_prompt")) then

            ! Allocate temporary array for chi_prompt
            allocate(temp_arr(1 * energy_groups * this % n_azi * this % n_pol))

            ! Get array for chi_prompt
            call get_node_array(node_xsdata, "chi_prompt", temp_arr)

            ! Initialize counter for temp_arr
            l = 0
            gin = 1
            do ipol = 1, this % n_pol
              do iazi = 1, this % n_azi
                do gout = 1, energy_groups
                  l = l + 1
                  this % chi_prompt(gout, gin, iazi, ipol) = temp_arr(l)
                end do

                ! Normalize chi so its CDF goes to 1
                this % chi_prompt(:, gin, iazi, ipol) = &
                     this % chi_prompt(:, gin, iazi, ipol) / &
                     sum(this % chi_prompt(:, gin, iazi, ipol))
              end do
            end do

            ! Now set all the other gin values
            do ipol = 1, this % n_pol
              do iazi = 1, this % n_azi
                do gin = 2, energy_groups
                  this % chi_prompt(:, gin, iazi, ipol) = &
                       this % chi_prompt(:, 1, iazi, ipol)
                end do
              end do
            end do

            ! Dellocate temporary array for chi_prompt
            deallocate(temp_arr)

          else
            call fatal_error("If chi and nu_fission not provided, chi_prompt &
                 &must be provided")
          end if

          ! Set chi_delayed
          if (check_for_node(node_xsdata, "chi_delayed")) then

            ! Allocate temporary array for chi_delayed
            allocate(temp_arr(1 * energy_groups * &
                 this % n_azi * this % n_pol * delayed_groups))

            ! Get array with chi_delayed
            call get_node_array(node_xsdata, "chi_delayed", temp_arr)

            ! Initialize counter for temp_arr
            l = 0
            gin = 1
            do ipol = 1, this % n_pol
              do iazi = 1, this % n_azi
                do gout = 1, energy_groups
                  do dg = 1, delayed_groups
                    l = l + 1
                    this % chi_delayed(gout, gin, iazi, ipol, dg) = temp_arr(l)
                  end do
                end do

                ! Normalize chi so its CDF goes to 1
                this % chi_delayed(:, gin, iazi, ipol, dg) = &
                     this % chi_delayed(:, gin, iazi, ipol, dg) / &
                     sum(this % chi_delayed(:, gin, iazi, ipol, dg))
              end do
            end do

            ! Now set all the other gin values
            do dg = 1, delayed_groups
              do ipol = 1, this % n_pol
                do iazi = 1, this % n_azi
                  do gin = 2, energy_groups
                    this % chi_delayed(:, gin, iazi, ipol, dg) = &
                         this % chi_delayed(:, 1, iazi, ipol, dg)
                  end do
                end do
              end do
            end do

            ! Deallocate temporary array for chi_delayed
            deallocate(temp_arr)

          else
            call fatal_error("If chi and nu_fission not provided, chi_delayed &
                 &must be provided")
          end if

          ! Get nu_fission (as a vector)
          if (check_for_node(node_xsdata, "nu_fission")) then

            ! Allocate temporary array for nu_fission
            allocate(temp_arr(energy_groups * this % n_azi * this % n_pol))

            ! Get nu_fission
            call get_node_array(node_xsdata, "nu_fission", temp_arr)
            this % prompt_nu_fission(:, :, :) = reshape(temp_arr, &
                 (/energy_groups, this % n_azi, this % n_pol/))

            ! Deallocate temporary array for nu_fission
            deallocate(temp_arr)

            ! ------------------------------------------------------------------
            ! a) If beta present, prompt_nu_fission = (1 - beta) * nu_fission
            !    and delayed_nu_fission_dg = beta_dg * nu_fission
            ! b) Else, prompt_nu_fission = nu_fission and delayed_nu_fission = 0
            ! ------------------------------------------------------------------
            do gin = 1, energy_groups
              do ipol = 1, this % n_pol
                do iazi = 1, this % n_azi
                  do dg = 1, delayed_groups

                    ! Set delayed_nu_fission using delayed neutron fraction
                    this % delayed_nu_fission(gin, iazi, ipol, dg) = &
                         temp_beta_3d(iazi, ipol, dg) * &
                         this % prompt_nu_fission(gin, iazi, ipol)
                  end do

                  ! Correct prompt_nu_fission using delayed neutron fraction
                  this % prompt_nu_fission(gin, iazi, ipol) = &
                       (1 - sum(temp_beta_3d(iazi, ipol, :))) * &
                       this % prompt_nu_fission(gin, iazi, ipol)
                end do
              end do
            end do
          else
            call fatal_error("If chi provided, nu_fission must be provided")
          end if

          ! Deallocate temporary beta arrays
          deallocate(temp_beta)
          deallocate(temp_beta_3d)

          ! --------------------------------------------------------------------
          ! 4) chi_prompt (v), chi_delayed (m), prompt_nu_fission (v)
          !    and delayed_nu_fission (v) provided
          ! --------------------------------------------------------------------
        else

          ! Set chi_prompt
          if (check_for_node(node_xsdata, "chi_prompt")) then

            ! Allocate temporary array for chi_prompt
            allocate(temp_arr(1 * energy_groups * this % n_azi * this % n_pol))

            ! Get array for chi_prompt
            call get_node_array(node_xsdata, "chi_prompt", temp_arr)

            ! Initialize counter for temp_arr
            l = 0
            gin = 1
            do ipol = 1, this % n_pol
              do iazi = 1, this % n_azi
                do gout = 1, energy_groups
                  l = l + 1
                  this % chi_prompt(gout, gin, iazi, ipol) = temp_arr(l)
                end do

                ! Normalize chi so its CDF goes to 1
                this % chi_prompt(:, gin, iazi, ipol) = &
                     this % chi_prompt(:, gin, iazi, ipol) / &
                     sum(this % chi_prompt(:, gin, iazi, ipol))
              end do
            end do

            ! Now set all the other gin values
            do ipol = 1, this % n_pol
              do iazi = 1, this % n_azi
                do gin = 2, energy_groups
                  this % chi_prompt(:, gin, iazi, ipol) = &
                       this % chi_prompt(:, 1, iazi, ipol)
                end do
              end do
            end do

            ! Dellocate temporary array for chi_prompt
            deallocate(temp_arr)

          else
            call fatal_error("If chi and nu_fission not provided, chi_prompt &
                 &must be provided")
          end if

          ! Set prompt_nu_fission
          if (check_for_node(node_xsdata, "prompt_nu_fission")) then

            ! Allocate temporaray array for prompt_nu_fission
            allocate(temp_arr(energy_groups * this % n_azi * this % n_pol))

            ! Get array for prompt_nu_fission
            call get_node_array(node_xsdata, "prompt_nu_fission", temp_arr)
            this % prompt_nu_fission(:, :, :) = reshape(temp_arr, &
                 (/energy_groups, this % n_azi, this % n_pol/))

            ! Deallocate temporary array for prompt_nu_fission
            deallocate(temp_arr)

          else
            call fatal_error("If chi and nu_fision not provided, &
                 &prompt_nu_fission must be provided")
          end if

          ! Set chi_delayed
          if (check_for_node(node_xsdata, "chi_delayed")) then

            ! Allocate temporary array for chi_delayed
            allocate(temp_arr(1 * energy_groups * &
                 this % n_azi * this % n_pol * delayed_groups))

            ! Get array with chi_delayed
            call get_node_array(node_xsdata, "chi_delayed", temp_arr)

            ! Initialize counter for temp_arr
            l = 0
            gin = 1
            do ipol = 1, this % n_pol
              do iazi = 1, this % n_azi
                do gout = 1, energy_groups
                  do dg = 1, delayed_groups
                    l = l + 1
                    this % chi_delayed(gout, gin, iazi, ipol, dg) = temp_arr(l)
                  end do
                end do

                ! Normalize chi so its CDF goes to 1
                this % chi_delayed(:, gin, iazi, ipol, dg) = &
                     this % chi_delayed(:, gin, iazi, ipol, dg) / &
                     sum(this % chi_delayed(:, gin, iazi, ipol, dg))
              end do
            end do

            ! Now set all the other gin values
            do dg = 1, delayed_groups
              do ipol = 1, this % n_pol
                do iazi = 1, this % n_azi
                  do gin = 2, energy_groups
                    this % chi_delayed(:, gin, iazi, ipol, dg) = &
                         this % chi_delayed(:, 1, iazi, ipol, dg)
                  end do
                end do
              end do
            end do

            ! Deallocate temporary array for chi_delayed
            deallocate(temp_arr)

          else
            call fatal_error("If chi and nu_fission not provided, chi_delayed &
                 &must be provided")
          end if

          ! Get delayed_nu_fission
          if (check_for_node(node_xsdata, "delayed_nu_fission")) then

            ! Allocate temporary array for delayed_nu_fission
            allocate(temp_arr(energy_groups * delayed_groups * &
                 this % n_azi * this % n_pol))

            ! Get array with delayed_nu_fission
            call get_node_array(node_xsdata, "delayed_nu_fission", temp_arr)
            this % delayed_nu_fission(:, :, :, :) = reshape(temp_arr, &
                 (/energy_groups, this % n_azi, this % n_pol, delayed_groups/))

            ! Deallocate temporary array for delayed_nu_fission
            deallocate(temp_arr)

          else
            call fatal_error("If chi and nu_fision not provided, &
                 &delayed_nu_fission must be provided")
          end if
        end if

        ! chi_prompt, chi_delayed, prompt_nu_fission, and delayed_nu_fission
        ! have been set; Now we will check for the rest of the XS that are
        ! unique to fissionable isotopes

        ! Set fission xs
        if (check_for_node(node_xsdata, "fission")) then

          ! Allocate temporary array for fission
          allocate(temp_arr(energy_groups * this % n_azi * this % n_pol))

          ! Get fission array
          call get_node_array(node_xsdata, "fission", temp_arr)
          this % fission(:, :, :) = reshape(temp_arr, (/energy_groups, &
               this % n_azi, this % n_pol/))

          ! Deallocate temporary array for fission
          deallocate(temp_arr)

        else
          this % fission = ZERO
        end if

        ! Set kappa_fission xs
        if (check_for_node(node_xsdata, "kappa_fission")) then

          ! Allocate temporary array for kappa_fission
          allocate(temp_arr(energy_groups * this % n_azi * this % n_pol))

          ! Get kappa_fission array
          call get_node_array(node_xsdata, "kappa_fission", temp_arr)
          this % kappa_fission(:, :, :) = reshape(temp_arr, (/energy_groups, &
               this % n_azi, this % n_pol/))

          ! Deallocate temporary array for kappa_fission
          deallocate(temp_arr)

        else
          this % kappa_fission = ZERO
        end if

        ! Set decay rate
        if (check_for_node(node_xsdata, "decay_rate")) then

          ! Allocate temporary array for decay_rate
          allocate(temp_arr(this % n_azi * this % n_pol * delayed_groups))

          ! Get decay_rate array
          call get_node_array(node_xsdata, "decay_rate", temp_arr)
          this % decay_rate(:, :, :) = reshape(temp_arr, (/this % n_azi, &
               this % n_pol, delayed_groups/))

          ! Deallocate temporary array for decay_rate
          deallocate(temp_arr)

        else
          this % decay_rate = ZERO
        end if

      else
        this % delayed_nu_fission(:, :, :, :) = ZERO
        this % prompt_nu_fission(:, :, :)     = ZERO
        this % chi_delayed(:, :, :, :, :)     = ZERO
        this % chi_prompt(:, :, :, :)         = ZERO
        this % fission(:, :, :)               = ZERO
        this % kappa_fission(:, :, :)         = ZERO
        this % decay_rate(:, :, :)            = ZERO
      end if

      ! All the XS unique to fissionable isotopes have been set; Now set all
      ! the generation XS

      ! Get absorption xs
      if (check_for_node(node_xsdata, "absorption")) then

        ! Allocate temporary array for decay_rate
        allocate(temp_arr(energy_groups * this % n_azi * this % n_pol))

        ! Get absorption array
        call get_node_array(node_xsdata, "absorption", temp_arr)
        this % absorption(:, :, :) = reshape(temp_arr, (/energy_groups, &
             this % n_azi, this % n_pol/))

        ! Deallocate temporary array for decay_rate
        deallocate(temp_arr)

      else
        call fatal_error("Must provide absorption!")
      end if

      ! Get velocity
      if (check_for_node(node_xsdata, "velocity")) then

        ! Allocate temporary array for decay_rate
        allocate(temp_arr(energy_groups * this % n_azi * this % n_pol))

        ! Get velocity array
        call get_node_array(node_xsdata, "velocity", temp_arr)
        this % velocity(:, :, :) = reshape(temp_arr, (/energy_groups, &
             this % n_azi, this % n_pol/))

        ! Deallocate temporary array for decay_rate
        deallocate(temp_arr)

      else
        this % velocity = ZERO
      end if

      ! Get multiplication data if present
      if (check_for_node(node_xsdata, "multiplicity")) then

        ! Allocate temporary 4D array for multiplicity
        allocate(temp_mult(energy_groups, energy_groups, this % n_azi, &
             this % n_pol))

        ! Get multiplicity data
        arr_len = get_arraysize_double(node_xsdata, "multiplicity")
        if (arr_len == energy_groups * energy_groups * this % n_azi * &
             this % n_pol) then

          ! Allocate temporary 1D array for multiplicity
          allocate(temp_arr(arr_len))

          ! Get multiplicity
          call get_node_array(node_xsdata, "multiplicity", temp_arr)
          temp_mult(:, :, :, :) = reshape(temp_arr, (/energy_groups, &
               energy_groups, this % n_azi, this % n_pol/))

          ! Deallocate temporary 1D array for multiplicity
          deallocate(temp_arr)
        else
          call fatal_error("Multiplicity length not same as number of groups&
                           & squared!")
        end if

        ! Deallocate temporary 4D array for multiplicity
        deallocate(temp_mult)

      else
        temp_mult(:, :, :, :) = ONE
      end if

      ! Get scattering treatment information
      ! Tabular_legendre tells us if we are to treat the provided
      ! Legendre polynomials as tabular data (if enable is true) or leaving
      ! them as Legendres (if enable is false, or the default)

      ! Set the default (leave as Legendre polynomials)
      enable_leg_mu = .false.
      if (check_for_node(node_xsdata, "tabular_legendre")) then
        call get_node_ptr(node_xsdata, "tabular_legendre", node_legendre_mu)
        if (check_for_node(node_legendre_mu, "enable")) then
          call get_node_value(node_legendre_mu, "enable", temp_str)
          temp_str = trim(to_lower(temp_str))
          if (temp_str == 'true' .or. temp_str == '1') then
            enable_leg_mu = .true.
          elseif (temp_str == 'false' .or. temp_str == '0') then
            enable_leg_mu = .false.
          else
            call fatal_error("Unrecognized tabular_legendre/enable: " &
                             // temp_str)
          end if
        end if

        ! Ok, so if we need to convert to a tabular form, get the user provided
        ! number of points
        if (enable_leg_mu) then
          if (check_for_node(node_legendre_mu, "num_points")) then
            call get_node_value(node_legendre_mu, "num_points", &
                 legendre_mu_points)
            if (legendre_mu_points <= 0) &
                 call fatal_error("num_points element must be positive&
                                  & and non-zero!")
          else
            ! Set the default number of points (0.0625 spacing)
            legendre_mu_points = 33
          end if
        end if
      end if

      ! Get the library's value for the order
      if (check_for_node(node_xsdata, "order")) then
        call get_node_value(node_xsdata, "order", order)
      else
        call fatal_error("Order must be provided!")
      end if

      ! Before retrieving the data, store the dimensionality of the data in
      ! order_dim.  For Legendre data, we usually refer to it as Pn where
      ! n is the order.  However Pn has n+1 sets of points (since you need to
      ! the count the P0 moment).  Adjust for that.  Histogram and Tabular
      ! formats dont need this adjustment.
      if (this % scatt_type == ANGLE_LEGENDRE) then
        order_dim = order + 1
      else
        order_dim = order
      end if

      ! The input is gathered in the more user-friendly facing format of
      ! Gout x Gin x Order x Azi x Pol.  We will get it in that format in
      ! input_scatt, but then need to convert it to a more useful ordering
      ! for processing (Order x Gout x Gin x Azi x Pol).
      allocate(input_scatt(energy_groups, energy_groups, order_dim, &
           this % n_azi, this % n_pol))
      if (check_for_node(node_xsdata, "scatter")) then
        allocate(temp_arr(energy_groups * energy_groups * order_dim * &
             this % n_azi * this % n_pol))
        call get_node_array(node_xsdata, "scatter", temp_arr)
        input_scatt(:, :, :, :, :) = reshape(temp_arr, (/energy_groups, &
             energy_groups, order_dim, this % n_azi, this % n_pol/))
        deallocate(temp_arr)

        ! Compare the number of orders given with the maximum order of the
        ! problem.  Strip off the supefluous orders if needed.
        if (this % scatt_type == ANGLE_LEGENDRE) then
          order = min(order_dim - 1, max_order)
          order_dim = order + 1
        end if

        allocate(temp_scatt(energy_groups, energy_groups, order_dim, &
             this % n_azi, this % n_pol))
        temp_scatt(:, :, :, :, :) = input_scatt(:, :, 1:order_dim, :, :)

        ! Take input format (groups, groups, order) and convert to
        ! the more useful format needed for scattdata: (order, groups, groups)
        ! However, if scatt_type was ANGLE_LEGENDRE (i.e., the data was
        ! provided as Legendre coefficients), and the user requested that
        ! these legendres be converted to tabular form (note this is also
        ! the default behavior), convert that now.
        if (this % scatt_type == ANGLE_LEGENDRE .and. enable_leg_mu) then

          ! Convert input parameters to what we need for the rest.
          this % scatt_type = ANGLE_TABULAR
          order_dim = legendre_mu_points
          order = order_dim
          dmu = TWO / real(order - 1, 8)

          allocate(scatt_coeffs(order_dim, energy_groups, energy_groups, &
               this % n_azi, this % n_pol))
          do ipol = 1, this % n_pol
            do iazi = 1, this % n_azi
              do gin = 1, energy_groups
                do gout = 1, energy_groups
                  norm = ZERO
                  do imu = 1, order_dim
                    if (imu == 1) then
                      mu = -ONE
                    else if (imu == order_dim) then
                      mu = ONE
                    else
                      mu = -ONE + real(imu - 1, 8) * dmu
                    end if
                    scatt_coeffs(imu, gout, gin, iazi, ipol) = &
                         evaluate_legendre(temp_scatt(gout, gin, :, iazi, ipol), mu)
                    ! Ensure positivity of distribution
                    if (scatt_coeffs(imu, gout, gin, iazi, ipol) < ZERO) &
                         scatt_coeffs(imu, gout, gin, iazi, ipol) = ZERO
                    ! And accrue the integral
                    if (imu > 1) then
                      norm = norm + HALF * dmu * &
                           (scatt_coeffs(imu - 1, gout, gin, iazi, ipol) + &
                            scatt_coeffs(imu, gout, gin, iazi, ipol))
                    end if
                  end do
                  ! Now that we have the integral, lets ensure that the distribution
                  ! is normalized such that it preserves the original scattering xs
                  if (norm > ZERO) then
                    scatt_coeffs(:, gout, gin, iazi, ipol) = &
                         scatt_coeffs(:, gout, gin, iazi, ipol) * &
                         temp_scatt(gout, gin, 1, iazi, ipol) / norm
                  end if
                end do
              end do
            end do
          end do
        else
          ! Sticking with current representation, carry forward but change
          ! the array ordering
          allocate(scatt_coeffs(order_dim, energy_groups, energy_groups, &
               this % n_azi, this % n_pol))
          do ipol = 1, this % n_pol
            do iazi = 1, this % n_azi
              do gin = 1, energy_groups
                do gout = 1, energy_groups
                  do l = 1, order_dim
                    scatt_coeffs(l, gout, gin, iazi, ipol) = &
                         temp_scatt(gout, gin, l, iazi, ipol)
                  end do
                end do
              end do
            end do
          end do
        end if
        deallocate(temp_scatt)
      else
        call fatal_error("Must provide scatter!")
      end if

      allocate(this % scatter(this % n_azi, this % n_pol))
      do ipol = 1, this % n_pol
        do iazi = 1,  this % n_azi
          ! Allocate and initialize our ScattData Object.
          if (this % scatt_type == ANGLE_HISTOGRAM) then
            allocate(ScattDataHistogram :: this % scatter(iazi, ipol) % obj)
          else if (this % scatt_type == ANGLE_TABULAR) then
            allocate(ScattDataTabular :: this % scatter(iazi, ipol) % obj)
          else if (this % scatt_type == ANGLE_LEGENDRE) then
            allocate(ScattDataLegendre :: this % scatter(iazi, ipol) % obj)
          end if

          ! Initialize the ScattData Object
          call this % scatter(iazi, ipol) % obj % init(&
               temp_mult(:, :, iazi, ipol), &
               scatt_coeffs(:, :, :, iazi, ipol))
        end do
      end do
      ! Deallocate temporaries for the next material
      deallocate(input_scatt, scatt_coeffs, temp_mult)

      allocate(this % total(energy_groups, this % n_azi, this % n_pol))
      if (check_for_node(node_xsdata, "total")) then
        allocate(temp_arr(energy_groups * this % n_azi * this % n_pol))
        call get_node_array(node_xsdata, "total", temp_arr)
        this % total(:, :, :) = reshape(temp_arr, (/energy_groups, &
             this % n_azi, this % n_pol/))
        deallocate(temp_arr)
      else
        do ipol = 1, this % n_pol
          do iazi = 1, this % n_azi
            this % total(:, iazi, ipol) = this % absorption(:, iazi, ipol) + &
                 this % scatter(iazi, ipol) % obj % scattxs(:)
          end do
        end do
      end if

    end subroutine mgxsang_init_file

!===============================================================================
! MGXS*_GET_XS returns the requested data cross section data
!===============================================================================

    pure function mgxsiso_get_xs(this, xstype, gin, gout, uvw, mu, dg) result(xs)
      class(MgxsIso), intent(in)    :: this   ! The Mgxs to initialize
      character(*) , intent(in)     :: xstype ! Type of xs requested
      integer, intent(in)           :: gin    ! Incoming energy group
      integer, optional, intent(in) :: gout   ! Outgoing energy group
      real(8), optional, intent(in) :: uvw(3) ! Requested angle
      real(8), optional, intent(in) :: mu     ! Change in angle
      integer, optional, intent(in) :: dg     ! Delayed group
      real(8)                       :: xs     ! Requested x/s

      select case(xstype)

      case('total')
        xs = this % total(gin)

      case('absorption')
        xs = this % absorption(gin)

      case('fission')
        xs = this % fission(gin)

      case('kappa_fission')
        xs = this % kappa_fission(gin)

      case('velocity')
        xs = this % velocity(gin)

      case('decay_rate')
        if (present(dg)) then
          xs = this % decay_rate(dg)
        else
          xs = this % decay_rate(1)
        end if

      case('prompt_nu_fission')
        xs = this % prompt_nu_fission(gin)

      case('delayed_nu_fission')
        if (present(dg)) then
          xs = this % delayed_nu_fission(gin, dg)
        else
          xs = sum(this % delayed_nu_fission(gin, :))
        end if

      case('nu_fission')
        xs = this % prompt_nu_fission(gin) + &
             sum(this % delayed_nu_fission(gin, :))

      case('nu')
        if (this % fission(gin) > ZERO) then
          xs = (sum(this % delayed_nu_fission(gin, :)) + &
               this % prompt_nu_fission(gin)) / this % fission(gin)
        else
          xs = ZERO
        end if

      case('nu_prompt')
        if (this % fission(gin) > ZERO) then
          xs = this % prompt_nu_fission(gin) / this % fission(gin)
        else
          xs = ZERO
        end if

      case('nu_delayed')
        if (this % fission(gin) > ZERO) then
          if (present(dg)) then
            xs = this % delayed_nu_fission(gin, dg) / this % fission(gin)
          else
            xs = sum(this % delayed_nu_fission(gin, :)) / this % fission(gin)
          end if
        else
          xs = ZERO
        end if

      case('chi_prompt')
        if (present(gout)) then
          xs = this % chi_prompt(gout,gin)
        else
          ! Not sure youd want a 1 or a 0, but here you go!
          xs = sum(this % chi_prompt(:, gin))
        end if

      case('chi_delayed')
        if (present(gout)) then
          if (present(dg)) then
            xs = this % chi_delayed(gout, gin, dg)
          else
            xs = this % chi_delayed(gout, gin, 1)
          end if
        else
          if (present(dg)) then
            xs = sum(this % chi_delayed(:, gin, dg))
          else
            xs = sum(this % chi_delayed(:, gin, 1))
          end if
        end if

      case('scatter')
        if (present(gout)) then
          if (gout < this % scatter % gmin(gin) .or. &
               gout > this % scatter % gmax(gin)) then
            xs = ZERO
          else
            xs = this % scatter % scattxs(gin) * &
                 this % scatter % energy(gin) % data(gout)
          end if
        else
          xs = this % scatter % scattxs(gin)
        end if

      case('scatter/mult')
        if (present(gout)) then
          if (gout < this % scatter % gmin(gin) .or. &
               gout > this % scatter % gmax(gin)) then
            xs = ZERO
          else
            xs = this % scatter % scattxs(gin) * &
                 this % scatter % energy(gin) % data(gout) / &
                 this % scatter % mult(gin) % data(gout)
          end if
        else
          xs = this % scatter % scattxs(gin) / &
               (dot_product(this % scatter % mult(gin) % data, &
                this % scatter % energy(gin) % data))
        end if

      case('scatter*f_mu/mult','scatter*f_mu')
        if (present(gout)) then
          if (gout < this % scatter % gmin(gin) .or. &
               gout > this % scatter % gmax(gin)) then
            xs = ZERO
          else
            xs = this % scatter % scattxs(gin) * &
                 this % scatter % energy(gin) % data(gout) * &
                 this % scatter % calc_f(gin, gout, mu)
            if (xstype == 'scatter*f_mu/mult') then
              xs = xs / this % scatter % mult(gin) % data(gout)
            end if
          end if
        else
          xs = ZERO
          ! TODO (Not likely needed)
          ! (asking for f_mu without asking for a group or mu would mean the
          ! user of this code wants the complete 1-outgoing group distribution
          ! which Im not sure what they would do with that.
        end if

      case default
        xs = ZERO

      end select

    end function mgxsiso_get_xs

    pure function mgxsang_get_xs(this, xstype, gin, gout, uvw, mu, dg) result(xs)
      class(MgxsAngle), intent(in)  :: this   ! The Mgxs to initialize
      character(*) , intent(in)     :: xstype ! Type of xs requested
      integer, intent(in)           :: gin    ! Incoming energy group
      integer, optional, intent(in) :: gout   ! Outgoing energy group
      real(8), optional, intent(in) :: uvw(3) ! Requested angle
      real(8), optional, intent(in) :: mu     ! Change in angle
      integer, optional, intent(in) :: dg     ! Delayed group
      real(8)                       :: xs     ! Requested x/s

      integer :: iazi, ipol

      if (present(uvw)) then

        call find_angle(this % polar, this % azimuthal, uvw, iazi, ipol)

        select case(xstype)

        case('total')
          xs = this % total(gin, iazi, ipol)

        case('absorption')
          xs = this % absorption(gin, iazi, ipol)

        case('fission')
          xs = this % fission(gin, iazi, ipol)

        case('kappa_fission')
          xs = this % kappa_fission(gin, iazi, ipol)

        case('prompt_nu_fission')
          xs = this % prompt_nu_fission(gin, iazi, ipol)

        case('delayed_nu_fission')
          if (present(dg)) then
            xs = this % delayed_nu_fission(gin, iazi, ipol, dg)
          else
            xs = sum(this % delayed_nu_fission(gin, iazi, ipol, :))
          end if

        case('nu_fission')
          xs = this % prompt_nu_fission(gin, iazi, ipol) + &
               sum(this % delayed_nu_fission(gin, iazi, ipol, :))

      case('nu')
        if (this % fission(gin, iazi, ipol) > ZERO) then
          xs = (sum(this % delayed_nu_fission(gin, iazi, ipol, :)) + &
               this % prompt_nu_fission(gin, iazi, ipol)) / &
               this % fission(gin, iazi, ipol)
        else
          xs = ZERO
        end if

      case('nu_prompt')
        if (this % fission(gin, iazi, ipol) > ZERO) then
          xs = this % prompt_nu_fission(gin, iazi, ipol) / &
               this % fission(gin, iazi, ipol)
        else
          xs = ZERO
        end if

      case('nu_delayed')
        if (this % fission(gin, iazi, ipol) > ZERO) then
          if (present(dg)) then
            xs = this % delayed_nu_fission(gin, iazi, ipol, dg) / &
                 this % fission(gin, iazi, ipol)
          else
            xs = sum(this % delayed_nu_fission(gin, iazi, ipol, :)) / &
                 this % fission(gin, iazi, ipol)
          end if
        else
          xs = ZERO
        end if

        case('chi_prompt')
          if (present(gout)) then
            xs = this % chi_prompt(gout, gin, iazi, ipol)
          else
            ! Not sure you would want a 1 or a 0, but here you go!
            xs = sum(this % chi_prompt(:, gin, iazi, ipol))
          end if

        case('chi_delayed')
          if (present(gout)) then
            if (present(dg)) then
              xs = this % chi_delayed(gout, gin, iazi, ipol, dg)
            else
              xs = this % chi_delayed(gout, gin, iazi, ipol, 1)
            end if
          else
            if (present(dg)) then
              xs = sum(this % chi_delayed(:, gin, iazi, ipol, dg))
            else
              xs = sum(this % chi_delayed(:, gin, iazi, ipol, 1))
            end if
          end if

        case('decay_rate')
          if (present(dg)) then
            xs = this % decay_rate(iazi, ipol, dg)
          else
            xs = this % decay_rate(iazi, ipol, 1)
          end if

        case('velocity')
          xs = this % velocity(gin, iazi, ipol)

        case('scatter')
          if (present(gout)) then
            if (gout < this % scatter(iazi, ipol) % obj % gmin(gin) .or. &
                 gout > this % scatter(iazi, ipol) % obj % gmax(gin)) then
              xs = ZERO
            else
              xs = this % scatter(iazi, ipol) % obj % scattxs(gin) * &
                   this % scatter(iazi, ipol) % obj % energy(gin) % data(gout)
            end if
          else
            xs = this % scatter(iazi, ipol) % obj % scattxs(gin)
          end if

        case('scatter/mult')
          if (present(gout)) then
            if (gout < this % scatter(iazi, ipol) % obj % gmin(gin) .or. &
                 gout > this % scatter(iazi, ipol) % obj % gmax(gin)) then
              xs = ZERO
            else
              xs = this % scatter(iazi, ipol) % obj % scattxs(gin) * &
                   this % scatter(iazi, ipol) % obj % energy(gin) % data(gout) / &
                   this % scatter(iazi, ipol) % obj % mult(gin) % data(gout)
            end if
          else
            xs = this % scatter(iazi, ipol) % obj % scattxs(gin) / &
                 (dot_product(this % scatter(iazi, ipol) % obj % mult(gin) % data, &
                  this % scatter(iazi, ipol) % obj % energy(gin) % data))
          end if

        case('scatter*f_mu/mult','scatter*f_mu')
          if (present(gout)) then
            if (gout < this % scatter(iazi, ipol) % obj % gmin(gin) .or. &
                 gout > this % scatter(iazi, ipol) % obj % gmax(gin)) then
              xs = ZERO
            else
              xs = this % scatter(iazi, ipol) % obj % scattxs(gin) * &
                   this % scatter(iazi, ipol) % obj % energy(gin) % data(gout)
              xs = xs * this % scatter(iazi, ipol) % obj % calc_f(gin, gout, mu)
              if (xstype == 'scatter*f_mu/mult') then
                xs = xs / &
                     this % scatter(iazi, ipol) % obj % mult(gin) % data(gout)
              end if
            end if
          else
            xs = ZERO
            ! TODO (Not likely needed)
            ! (asking for f_mu without asking for a group or mu would mean the
            ! user of this code wants the complete 1-outgoing group distribution
            ! which Im not sure what they would do with that.
          end if

        case default
          xs = ZERO
        end select

      else
        xs = ZERO
      end if

    end function mgxsang_get_xs

!===============================================================================
! MACROXS*_COMBINE Builds a macroscopic Mgxs object from microscopic Mgxs
! objects
!===============================================================================

    subroutine mgxs_combine(this, mat, scatt_type)
      class(Mgxs), intent(inout)          :: this ! The Mgxs to initialize
      type(Material), pointer, intent(in) :: mat  ! base material
      integer, intent(in)                 :: scatt_type ! How is data presented

      ! Fill in meta-data from material information
      if (mat % name == "") then
        this % name      = trim(to_str(mat % id))
      else
        this % name      = mat % name
      end if

      this % fissionable = mat % fissionable
      this % scatt_type  = scatt_type

      ! The following info we should initialize, but we dont need it nor
      ! does it have guaranteed meaning.
      this % awr = -ONE
      this % kT  = -ONE

    end subroutine mgxs_combine

    subroutine mgxsiso_combine(this, mat, nuclides, energy_groups, &
         delayed_groups, max_order, scatt_type)
      class(MgxsIso), intent(inout)       :: this ! The Mgxs to initialize
      type(Material), pointer, intent(in) :: mat  ! base material
      type(MgxsContainer), intent(in)     :: nuclides(:) ! List of nuclides to harvest from
      integer, intent(in)                 :: energy_groups  ! Energy groups
      integer, intent(in)                 :: delayed_groups ! Delayed groups
      integer, intent(in)                 :: max_order  ! Maximum requested order
      integer, intent(in)                 :: scatt_type ! How is data presented

      integer :: i             ! loop index over nuclides
      integer :: gin, gout     ! group indices
      real(8) :: atom_density  ! atom density of a nuclide
      real(8) :: norm, nuscatt
      integer :: mat_max_order, order, order_dim, nuc_order_dim
      real(8), allocatable :: temp_mult(:, :), mult_num(:, :), mult_denom(:, :)
      real(8), allocatable :: scatt_coeffs(:, :, :)

      ! Set the meta-data
      call mgxs_combine(this, mat, scatt_type)

      ! Determine the scattering type of our data and ensure all scattering orders
      ! are the same.
      select type(nuc => nuclides(mat % nuclide(1)) % obj)
      type is (MgxsIso)
        order = size(nuc % scatter % dist(1) % data, dim=1)
      end select

      ! If we have tabular only data, then make sure all datasets have same size
      if (scatt_type == ANGLE_HISTOGRAM) then
        ! Check all scattering data to ensure it is the same size
        do i = 2, mat % n_nuclides
          select type(nuc => nuclides(mat % nuclide(i)) % obj)
          type is (MgxsIso)
            if (order /= size(nuc % scatter % dist(1) % data, dim=1)) &
                 call fatal_error("All histogram scattering entries must be&
                                  & same length!")
          end select
        end do

        ! Ok, got our order, store the dimensionality
        order_dim = order

        ! Set our Scatter Object Type
        allocate(ScattDataHistogram :: this % scatter)

      else if (scatt_type == ANGLE_TABULAR) then
        ! Check all scattering data to ensure it is the same size
        do i = 2, mat % n_nuclides
          select type(nuc => nuclides(mat % nuclide(i)) % obj)
          type is (MgxsIso)
            if (order /= size(nuc % scatter % dist(1) % data, dim=1)) &
                 call fatal_error("All tabular scattering entries must be&
                                  & same length!")
          end select
        end do

        ! Ok, got our order, store the dimensionality
        order_dim = order

        ! Set our Scatter Object Type
        allocate(ScattDataTabular :: this % scatter)

      else if (scatt_type == ANGLE_LEGENDRE) then
        ! Need to determine the maximum scattering order of all data in this material
        mat_max_order = 0
        do i = 1, mat % n_nuclides
          select type(nuc => nuclides(mat % nuclide(i)) % obj)
          type is (MgxsIso)
            if (size(nuc % scatter % dist(1) % data, dim=1) > mat_max_order) &
                 mat_max_order = size(nuc % scatter % dist(1) % data, dim=1)
          end select
        end do

        ! Now need to compare this material maximum scattering order with
        ! the problem wide max scatt order and use whichever is lower
        order = min(mat_max_order, max_order)

        ! Ok, got our order, store the dimensionality
        order_dim = order + 1

        ! Set our Scatter Object Type
        allocate(ScattDataLegendre :: this % scatter)
      end if

      ! Allocate and initialize data needed for macro_xs(i_mat) object
      allocate(this % total(energy_groups))
      this % total(:) = ZERO

      allocate(this % absorption(energy_groups))
      this % absorption(:) = ZERO

      allocate(this % fission(energy_groups))
      this % fission(:) = ZERO

      allocate(this % kappa_fission(energy_groups))
      this % kappa_fission(:) = ZERO

      allocate(this % prompt_nu_fission(energy_groups))
      this % prompt_nu_fission(:) = ZERO

      allocate(this % delayed_nu_fission(energy_groups, delayed_groups))
      this % delayed_nu_fission(:, :) = ZERO

      allocate(this % chi_prompt(energy_groups, energy_groups))
      this % chi_prompt(:, :) = ZERO

      allocate(this % chi_delayed(energy_groups, energy_groups, delayed_groups))
      this % chi_delayed(:, :, :) = ZERO

      allocate(this % velocity(energy_groups))
      this % velocity(:) = ZERO

      allocate(this % decay_rate(delayed_groups))
      this % decay_rate(:) = ZERO

      allocate(temp_mult(energy_groups,energy_groups))
      temp_mult(:, :) = ZERO

      allocate(mult_num(energy_groups,energy_groups))
      mult_num(:, :) = ZERO

      allocate(mult_denom(energy_groups,energy_groups))
      mult_denom(:, :) = ZERO

      allocate(scatt_coeffs(order_dim,energy_groups,energy_groups))
      scatt_coeffs(:, :, :) = ZERO

      ! Add contribution from each nuclide in material
      do i = 1, mat % n_nuclides
        ! Copy atom density of nuclide in material
        atom_density = mat % atom_density(i)

        ! Perform our operations which depend upon the type
        select type(nuc => nuclides(mat % nuclide(i)) % obj)
        type is (MgxsIso)
          ! Add contributions to total, absorption, and fission data (if necessary)
          this % total(:) = this % total(:) + atom_density * nuc % total(:)

          this % absorption(:) = this % absorption(:) + &
               atom_density * nuc % absorption(:)

          this % decay_rate(:) = this % decay_rate(:) + &
               atom_density * nuc % decay_rate(:)

          this % velocity(:) = this % velocity(:) + &
               atom_density * nuc % velocity(:)

          if (nuc % fissionable) then
            this % chi_prompt(:, :) = this % chi_prompt(:, :) + &
                 atom_density * nuc % chi_prompt(:, :)

            this % chi_delayed(:, :, :) = this % chi_delayed(:, :, :) + &
                 atom_density * nuc % chi_delayed(:, :, :)

            this % prompt_nu_fission(:) = this % prompt_nu_fission(:)+ &
                 atom_density * nuc % prompt_nu_fission(:)

            this % delayed_nu_fission(:,:) = this % delayed_nu_fission(:,:)+ &
                 atom_density * nuc % delayed_nu_fission(:,:)

            this % fission(:) = this % fission(:) + &
                 atom_density * nuc % fission(:)

            this % kappa_fission(:) = this % kappa_fission(:) + &
                 atom_density * nuc % kappa_fission(:)
          end if

          ! Get the multiplication matrix
          ! To combine from nuclidic data we need to use the final relationship
          ! mult_{gg'} = sum_i(N_i*nuscatt_{i,g,g'}) /
          !              sum_i(N_i*(nuscatt_{i,g,g'} / mult_{i,g,g'}))
          ! Developed as follows:
          ! mult_{gg'} = nuScatt{g,g'} / Scatt{g,g'}
          ! mult_{gg'} = sum_i(N_i*nuscatt_{i,g,g'}) / sum(N_i*scatt_{i,g,g'})
          ! mult_{gg'} = sum_i(N_i*nuscatt_{i,g,g'}) /
          !              sum_i(N_i*(nuscatt_{i,g,g'} / mult_{i,g,g'}))
          ! nuscatt_{i,g,g'} can be reconstructed from scatter % energy and
          ! scatter % scattxs
          do gin = 1, energy_groups
            do gout = nuc % scatter % gmin(gin), nuc % scatter % gmax(gin)

              nuscatt = nuc % scatter % scattxs(gin) * &
                   nuc % scatter % energy(gin) % data(gout)

              mult_num(gout, gin) = mult_num(gout, gin) + atom_density * &
                   nuscatt

              if (nuc % scatter % mult(gin) % data(gout) > ZERO) then
                mult_denom(gout, gin) = mult_denom(gout,gin) + atom_density * &
                     nuscatt / nuc % scatter % mult(gin) % data(gout)
              else
                ! Avoid division by zero
                mult_denom(gout, gin) = mult_denom(gout,gin) + atom_density
              end if
            end do
          end do

          ! Get the complete scattering matrix
          nuc_order_dim = size(nuc % scatter % dist(1) % data, dim=1)
          scatt_coeffs(1:min(nuc_order_dim, order_dim), :, :) = &
               scatt_coeffs(1:min(nuc_order_dim, order_dim), :, :) + &
               atom_density * &
               nuc % scatter % get_matrix(min(nuc_order_dim, order_dim))

        type is (MgxsAngle)
          call fatal_error("Invalid passing of MgxsAngle to MgxsIso object")
        end select
      end do

      ! Obtain temp_mult
      do gin = 1, energy_groups
        do gout = 1, energy_groups
          if (mult_denom(gout, gin) > ZERO) then
            temp_mult(gout, gin) = mult_num(gout, gin) / mult_denom(gout, gin)
          else
            temp_mult(gout, gin) = ONE
          end if
        end do
      end do

      ! Initialize the ScattData Object
      call this % scatter % init(temp_mult, scatt_coeffs)

      ! Deallocate temporaries
      deallocate(scatt_coeffs, temp_mult, mult_num, mult_denom)

    end subroutine mgxsiso_combine

    subroutine mgxsang_combine(this, mat, nuclides, energy_groups, &
         delayed_groups, max_order, scatt_type)
      class(MgxsAngle), intent(inout)     :: this ! The Mgxs to initialize
      type(Material), pointer, intent(in) :: mat  ! base material
      type(MgxsContainer), intent(in)     :: nuclides(:) ! List of nuclides to harvest from
      integer, intent(in)                 :: energy_groups  ! Energy groups
      integer, intent(in)                 :: delayed_groups ! Delayed groups
      integer, intent(in)                 :: max_order  ! Maximum requested order
      integer, intent(in)                 :: scatt_type ! Legendre or Tabular Scatt?

      integer :: i             ! loop index over nuclides
      integer :: gin, gout     ! group indices
      integer :: dg            ! delayed group indices
      real(8) :: atom_density  ! atom density of a nuclide
      integer :: ipol, iazi, n_pol, n_azi
      real(8) :: norm, nuscatt
      integer :: mat_max_order, order, order_dim, nuc_order_dim
      real(8), allocatable :: temp_mult(:, :, :, :), mult_num(:, :, :, :)
      real(8), allocatable :: mult_denom(:, :, :, :), scatt_coeffs(:, :, :, :, :)

      ! Set the meta-data
      call mgxs_combine(this, mat, scatt_type)

      ! Get the number of each polar and azi angles and make sure all the
      ! NuclideAngle types have the same number of these angles
      n_pol = -1
      n_azi = -1
      do i = 1, mat % n_nuclides

        select type(nuc => nuclides(mat % nuclide(i)) % obj)
        type is (MgxsAngle)

          if (n_pol == -1) then
            n_pol = nuc % n_pol
            n_azi = nuc % n_azi

            allocate(this % polar(n_pol))
            this % polar(:) = nuc % polar(:)

            allocate(this % azimuthal(n_azi))
            this % azimuthal(:) = nuc % azimuthal(:)
          else
            if ((n_pol /= nuc % n_pol) .or. (n_azi /= nuc % n_azi)) then
              call fatal_error("All angular data must be same length!")
            end if
          end if
        end select
      end do

      ! Determine the scattering type of our data and ensure all scattering orders
      ! are the same.
      select type(nuc => nuclides(mat % nuclide(1)) % obj)
      type is (MgxsAngle)
        order = size(nuc % scatter(1,1) % obj % dist(1) % data, dim=1)
      end select
      ! If we have tabular only data, then make sure all datasets have same size
      if (scatt_type == ANGLE_HISTOGRAM) then
        ! Check all scattering data to ensure it is the same size
        ! order = size(nuclides(mat % nuclide(1)) % obj % scatter % data,dim=1)
        do i = 2, mat % n_nuclides
          select type(nuc => nuclides(mat % nuclide(i)) % obj)
          type is (MgxsAngle)
            if (order /= size(nuc % scatter(1,1) % obj % dist(1) % data, dim=1)) &
                 call fatal_error("All histogram scattering entries must be&
                                  & same length!")
          end select
        end do
        ! Ok, got our order, store the dimensionality
        order_dim = order

        ! Set our Scatter Object Type
        allocate(this % scatter(n_azi, n_pol))
        do ipol = 1, n_pol
          do iazi = 1, n_azi
            allocate(ScattDataHistogram :: this % scatter(iazi, ipol) % obj)
          end do
        end do

      else if (scatt_type == ANGLE_TABULAR) then
        ! Check all scattering data to ensure it is the same size
        do i = 2, mat % n_nuclides
          select type(nuc => nuclides(mat % nuclide(i)) % obj)
          type is (MgxsAngle)
            if (order /= size(nuc % scatter(1, 1) % obj % dist(1) % data, dim=1)) &
                 call fatal_error("All tabular scattering entries must be&
                                  & same length!")
          end select
        end do
        ! Ok, got our order, store the dimensionality
        order_dim = order

        ! Set our Scatter Object Type
        allocate(this % scatter(n_azi, n_pol))
        do ipol = 1, n_pol
          do iazi = 1, n_azi
            allocate(ScattDataTabular :: this % scatter(iazi, ipol) % obj)
          end do
        end do

      else if (scatt_type == ANGLE_LEGENDRE) then
        ! Need to determine the maximum scattering order of all data in this material
        mat_max_order = 0
        do i = 1, mat % n_nuclides
          select type(nuc => nuclides(mat % nuclide(i)) % obj)
          type is (MgxsAngle)
            if (size(nuc % scatter(1,1) % obj % dist(1) % data, dim=1) > mat_max_order) &
                 mat_max_order = size(nuc % scatter(1,1) % obj% dist(1) % data, dim=1)
          end select
        end do

        ! Now need to compare this material maximum scattering order with
        ! the problem wide max scatt order and use whichever is lower
        order = min(mat_max_order, max_order)
        ! Ok, got our order, store the dimensionality
        order_dim = order + 1

        ! Set our Scatter Object Type
        allocate(this % scatter(n_azi, n_pol))
        do ipol = 1, n_pol
          do iazi = 1, n_azi
            allocate(ScattDataLegendre :: this % scatter(iazi, ipol) % obj)
          end do
        end do
      end if

      ! Allocate and initialize data within macro_xs(i_mat) object
      allocate(this % total(energy_groups, n_azi, n_pol))
      this % total(:, :, :) = ZERO

      allocate(this % absorption(energy_groups, n_azi, n_pol))
      this % absorption(:, :, :) = ZERO

      allocate(this % fission(energy_groups, n_azi, n_pol))
      this % fission(:, :, :) = ZERO

      allocate(this % decay_rate(n_azi, n_pol, delayed_groups))
      this % decay_rate(:, :, :) = ZERO

      allocate(this % velocity(energy_groups, n_azi, n_pol))
      this % velocity(:, :, :) = ZERO

      allocate(this % kappa_fission(energy_groups, n_azi, n_pol))
      this % kappa_fission(:, :, :) = ZERO

      allocate(this % prompt_nu_fission(energy_groups, n_azi, n_pol))
      this % prompt_nu_fission(:, :, :) = ZERO

      allocate(this % delayed_nu_fission(energy_groups, n_azi, n_pol, delayed_groups))
      this % delayed_nu_fission(:, :, :, :) = ZERO

      allocate(this % chi_prompt(energy_groups, energy_groups, n_azi, n_pol))
      this % chi_prompt(:, :, :, :) = ZERO

      allocate(this % chi_delayed(energy_groups, energy_groups, n_azi, n_pol, &
           delayed_groups))
      this % chi_delayed(:, :, :, :, :) = ZERO

      allocate(temp_mult(energy_groups, energy_groups, n_azi, n_pol))
      temp_mult(:, :, :, :) = ZERO

      allocate(mult_num(energy_groups, energy_groups, n_azi, n_pol))
      mult_num(:, :, :, :) = ZERO

      allocate(mult_denom(energy_groups, energy_groups, n_azi, n_pol))
      mult_denom(:, :, :, :) = ZERO

      allocate(scatt_coeffs(order_dim, energy_groups, energy_groups, n_azi, n_pol))
      scatt_coeffs(:, :, :, :, :) = ZERO

      ! Add contribution from each nuclide in material
      do i = 1, mat % n_nuclides
        ! Copy atom density of nuclide in material
        atom_density = mat % atom_density(i)

        ! Perform our operations which depend upon the type
        select type(nuc => nuclides(mat % nuclide(i)) % obj)

        type is (MgxsIso)
          call fatal_error("Invalid passing of MgxsIso to MgxsAngle object")

        type is (MgxsAngle)

          ! Add contributions to total, absorption, and fission data (if necessary)
          this % total(:, :, :) = this % total(:, :, :) + &
               atom_density * nuc % total(:, :, :)

          this % absorption(:, :, :) = this % absorption(:, :, :) + &
               atom_density * nuc % absorption(:, :, :)

          this % decay_rate(:, :, :) = this % decay_rate(:, :, :) + &
               atom_density * nuc % decay_rate(:, :, :)

          this % velocity(:, :, :) = this % velocity(:, :, :) + &
               atom_density * nuc % velocity(:, :, :)

          if (nuc % fissionable) then

            this % chi_prompt = this % chi_prompt + &
                 atom_density * nuc % chi_prompt

            this % chi_delayed = this % chi_delayed + &
                 atom_density * nuc % chi_delayed

            this % prompt_nu_fission(:, :, :) = &
                 this % prompt_nu_fission(:, :, :) + &
                 atom_density * nuc % prompt_nu_fission(:, :, :)

            this % delayed_nu_fission(:, :, :, :) = &
                 this % delayed_nu_fission(:, :, :, :) + &
                 atom_density * nuc % delayed_nu_fission(:, :, :, :)

            this % fission(:, :, :) = this % fission(:, :, :) + &
                 atom_density * nuc % fission(:, :, :)

            this % kappa_fission(:, :, :) = this % kappa_fission(:, :, :) + &
                 atom_density * nuc % kappa_fission(:, :, :)
          end if

          ! Get the multiplication matrix
          ! To combine from nuclidic data we need to use the final relationship
          ! mult_{gg'} = sum_i(N_i*nuscatt_{i,g,g'}) /
          !              sum_i(N_i*(nuscatt_{i,g,g'} / mult_{i,g,g'}))
          ! Developed as follows:
          ! mult_{gg'} = nuScatt{g,g'} / Scatt{g,g'}
          ! mult_{gg'} = sum_i(N_i*nuscatt_{i,g,g'}) / sum(N_i*scatt_{i,g,g'})
          ! mult_{gg'} = sum_i(N_i*nuscatt_{i,g,g'}) /
          !              sum_i(N_i*(nuscatt_{i,g,g'} / mult_{i,g,g'}))
          ! nuscatt_{i,g,g'} can be reconstructed from scatter % energy and
          ! scatter % scattxs
          do ipol = 1, n_pol
            do iazi = 1, n_azi
              do gin = 1, energy_groups
                do gout = nuc % scatter(iazi, ipol) % obj % gmin(gin), &
                     nuc % scatter(iazi, ipol) % obj % gmax(gin)

                  nuscatt = nuc % scatter(iazi, ipol) % obj % scattxs(gin) * &
                       nuc % scatter(iazi, ipol) % obj % energy(gin) % data(gout)

                  mult_num(gout, gin, iazi, ipol) = mult_num(gout, gin, iazi, ipol) + &
                       atom_density * nuscatt

                  if (nuc % scatter(iazi, ipol) % obj % mult(gin) % data(gout) > ZERO) then
                    mult_denom(gout, gin, iazi, ipol) = &
                         mult_denom(gout, gin, iazi, ipol) + &
                         atom_density * nuscatt / &
                         nuc % scatter(iazi, ipol) % obj % mult(gin) % data(gout)
                  else
                    ! Avoid division by zero
                    mult_denom(gout, gin, iazi, ipol) = &
                         mult_denom(gout,gin, iazi, ipol) + atom_density
                  end if
                end do
              end do
            end do
          end do

          ! Get the complete scattering matrix
          nuc_order_dim = size(nuc % scatter(1, 1) % obj % dist(1) % data, dim=1)
          do ipol = 1, n_pol
            do iazi = 1, n_azi
              scatt_coeffs(1:min(nuc_order_dim, order_dim), :, :, iazi, ipol) = &
                   scatt_coeffs(1:min(nuc_order_dim, order_dim), :, :, iazi, ipol) + &
                   atom_density * nuc % scatter(iazi, ipol) % obj % get_matrix(&
                   min(nuc_order_dim, order_dim))
            end do
          end do
        end select
      end do

      ! Obtain temp_mult
      do ipol = 1, n_pol
        do iazi = 1, n_azi
          do gin = 1, energy_groups
            do gout = 1, energy_groups
              if (mult_denom(gout, gin, iazi, ipol) > ZERO) then
                temp_mult(gout, gin, iazi, ipol) = &
                     mult_num(gout, gin, iazi, ipol) / &
                     mult_denom(gout, gin, iazi, ipol)
              else
                temp_mult(gout, gin, iazi, ipol) = ONE
              end if
            end do
          end do
        end do
      end do

      ! Initialize the ScattData Object
      do ipol = 1, n_pol
        do iazi = 1, n_azi
          call this % scatter(iazi, ipol) % obj % init( &
               temp_mult(:, :, iazi, ipol), scatt_coeffs(:, :, :, iazi, ipol))
        end do
      end do

      ! Now normalize chi
      if (mat % fissionable) then
        do ipol = 1, n_pol
          do iazi = 1, n_azi
            do gin = 1, energy_groups
              norm =  sum(this % chi_prompt(:, gin, iazi, ipol))
              if (norm > ZERO) then
                this % chi_prompt(:, gin, iazi, ipol) = &
                     this % chi_prompt(:, gin, iazi, ipol) / norm
              end if
            end do
          end do
        end do

        do dg = 1, delayed_groups
          do ipol = 1, n_pol
            do iazi = 1, n_azi
              do gin = 1, energy_groups
                norm =  sum(this % chi_delayed(:, gin, iazi, ipol, dg))
                if (norm > ZERO) then
                  this % chi_delayed(:, gin, iazi, ipol, dg) = &
                       this % chi_delayed(:, gin, iazi, ipol, dg) / norm
                end if
              end do
            end do
          end do
        end do
      end if

      ! Deallocate temporaries for the next material
      deallocate(scatt_coeffs, temp_mult)

    end subroutine mgxsang_combine

!===============================================================================
! MGXS*_SAMPLE_FISSION_ENERGY samples the outgoing energy from a fission event
!===============================================================================

    subroutine mgxsiso_sample_fission_energy(this, gin, uvw, dg, gout)
      class(MgxsIso), intent(in)    :: this   ! Data to work with
      integer, intent(in)           :: gin    ! Incoming energy group
      real(8), intent(in)           :: uvw(3) ! Particle Direction
      integer, intent(out)          :: dg     ! Delayed group
      integer, intent(out)          :: gout   ! Sampled outgoing group
      real(8) :: xi_pd            ! Our random number for prompt/delayed
      real(8) :: xi_gout          ! Our random number for gout
      real(8) :: prob_pd          ! Running probability for prompt/delayed
      real(8) :: prob_gout        ! Running probability for gout

      ! Get nu and nu_prompt
      real(8) :: nu, nu_prompt
      nu = this % get_xs('nu', gin)
      nu_prompt = this % get_xs('nu_prompt', gin)

      ! Sample random numbers
      xi_pd = prn()
      xi_gout = prn()

      ! Neutron is born prompt
      if (xi_pd < nu_prompt / nu) then

        ! set the delayed group for the particle born from fission to 0
        dg = 0

        gout = 1
        prob_gout = this % chi_prompt(gout, gin)

        do while (prob_gout < xi_gout)
          gout = gout + 1
          prob_gout = prob_gout + this % chi_prompt(gout, gin)
        end do

        ! Neutron is born delayed
      else

        ! Get the delayed group
        dg = 0
        prob_pd = nu_prompt / nu

        do while (xi_pd >= prob_pd)
          dg = dg + 1
          prob_pd = prob_pd + this % get_xs('nu_delayed', gin, dg=dg) &
               / nu
        end do

        ! Adjust dg in case of round off error
        dg = min(dg, num_delayed_groups)

        ! Get the outgoing group
        gout = 1
        prob_gout = this % chi_delayed(gout, gin, dg)

        do while (prob_gout < xi_gout)
          gout = gout + 1
          prob_gout = prob_gout + this % chi_delayed(gout, gin, dg)
        end do
      end if

    end subroutine mgxsiso_sample_fission_energy

    subroutine mgxsang_sample_fission_energy(this, gin, uvw, dg, gout)
      class(MgxsAngle), intent(in) :: this  ! Data to work with
      integer, intent(in)          :: gin    ! Incoming energy group
      real(8), intent(in)          :: uvw(3) ! Direction vector
      integer, intent(out)         :: dg     ! Delayed group
      integer, intent(out)         :: gout   ! Sampled outgoing group
      real(8) :: xi_pd            ! Our random number for prompt/delayed
      real(8) :: xi_gout          ! Our random number for gout
      real(8) :: prob_pd          ! Running probability for prompt/delayed
      real(8) :: prob_gout        ! Running probability for gout
      real(8) :: nu, nu_prompt
      integer :: iazi, ipol

      call find_angle(this % polar, this % azimuthal, uvw, iazi, ipol)

      ! Get nu and nu_prompt
      nu = this % get_xs('nu', gin, uvw=uvw)
      nu_prompt = this % get_xs('nu_prompt', gin, uvw=uvw)

      ! Sample random numbers
      xi_pd = prn()
      xi_gout = prn()

      ! Neutron is born prompt
      if (xi_pd < nu_prompt / nu) then

        ! set the delayed group for the particle born from fission to 0
        dg = 0

        gout = 1
        prob_gout = this % chi_prompt(gout, gin, iazi, ipol)

        do while (prob_gout < xi_gout)
          gout = gout + 1
          prob_gout = prob_gout + this % chi_prompt(gout, gin, iazi, ipol)
        end do

        ! Neutron is born delayed
      else

        ! Get the delayed group
        dg = 0
        prob_pd = nu_prompt / nu

        do while (xi_pd < prob_pd)
          dg = dg + 1
          prob_pd = prob_pd + &
               this % get_xs('nu_delayed', gin, uvw=uvw, dg=dg) &
               / nu
        end do

        ! Adjust dg in case of round off error
        dg = min(dg, num_delayed_groups)

        ! Get the outgoing group
        gout = 1
        prob_gout = this % chi_delayed(gout, gin, iazi, ipol, dg)

        do while (prob < xi_gout)
          gout = gout + 1
          prob_gout = prob_gout + this % chi_delayed(gout, gin, iazi, ipol, dg)
        end do
      end if

    end subroutine mgxsang_sample_fission_energy

!===============================================================================
! MGXS*_SAMPLE_SCATTER Selects outgoing energy and angle after a scatter event
!===============================================================================

    subroutine mgxsiso_sample_scatter(this, uvw, gin, gout, mu, wgt)
      class(MgxsIso), intent(in)    :: this
      real(8),           intent(in)    :: uvw(3) ! Incoming neutron direction
      integer,           intent(in)    :: gin    ! Incoming neutron group
      integer,           intent(out)   :: gout   ! Sampled outgoin group
      real(8),           intent(out)   :: mu     ! Sampled change in angle
      real(8),           intent(inout) :: wgt    ! Particle weight

      call this % scatter % sample(gin, gout, mu, wgt)

    end subroutine mgxsiso_sample_scatter

    subroutine mgxsang_sample_scatter(this, uvw, gin, gout, mu, wgt)
      class(MgxsAngle), intent(in)    :: this
      real(8),             intent(in)    :: uvw(3) ! Incoming neutron direction
      integer,             intent(in)    :: gin    ! Incoming neutron group
      integer,             intent(out)   :: gout   ! Sampled outgoin group
      real(8),             intent(out)   :: mu     ! Sampled change in angle
      real(8),             intent(inout) :: wgt    ! Particle weight

      integer :: iazi, ipol ! Angular indices

      call find_angle(this % polar, this % azimuthal, uvw, iazi, ipol)
      call this % scatter(iazi, ipol) % obj % sample(gin, gout, mu, wgt)

    end subroutine mgxsang_sample_scatter

!===============================================================================
! MGXS*_CALCULATE_XS determines the multi-group cross sections
! for the material the particle is currently traveling through.
!===============================================================================

    subroutine mgxsiso_calculate_xs(this, gin, uvw, xs)
      class(MgxsIso),        intent(in)    :: this
      integer,               intent(in)    :: gin    ! Incoming neutron group
      real(8),               intent(in)    :: uvw(3) ! Incoming neutron direction
      type(MaterialMacroXS), intent(inout) :: xs     ! Resultant Mgxs Data

      xs % total         = this % total(gin)
      xs % elastic       = this % scatter % scattxs(gin)
      xs % absorption    = this % absorption(gin)
      xs % fission       = this % fission(gin)
      xs % nu_fission    = this % prompt_nu_fission(gin) + &
           sum(this % delayed_nu_fission(gin, :))

    end subroutine mgxsiso_calculate_xs

    subroutine mgxsang_calculate_xs(this, gin, uvw, xs)
      class(MgxsAngle),      intent(in)    :: this
      integer,               intent(in)    :: gin    ! Incoming neutron group
      real(8),               intent(in)    :: uvw(3) ! Incoming neutron direction
      type(MaterialMacroXS), intent(inout) :: xs     ! Resultant Mgxs Data

      integer :: iazi, ipol

      call find_angle(this % polar, this % azimuthal, uvw, iazi, ipol)
      xs % total         = this % total(gin, iazi, ipol)
      xs % elastic       = this % scatter(iazi, ipol) % obj % scattxs(gin)
      xs % absorption    = this % absorption(gin, iazi, ipol)
      xs % fission       = this % fission(gin, iazi, ipol)
      xs % nu_fission    = this % prompt_nu_fission(gin, iazi, ipol) + &
           sum(this % delayed_nu_fission(gin, iazi, ipol, :))

    end subroutine mgxsang_calculate_xs

!===============================================================================
! find_angle finds the closest angle on the data grid and returns that index
!===============================================================================

    pure subroutine find_angle(polar, azimuthal, uvw, i_azi, i_pol)
      real(8), intent(in) :: polar(:)     ! Polar angles [0,pi]
      real(8), intent(in) :: azimuthal(:) ! Azi. angles [-pi,pi]
      real(8), intent(in) :: uvw(3)       ! Direction of motion
      integer, intent(inout) :: i_pol     ! Closest polar bin
      integer, intent(inout) :: i_azi     ! Closest azi bin

      real(8) :: my_pol, my_azi, dangle

      ! Convert uvw to polar and azi
      my_pol = acos(uvw(3))
      my_azi = atan2(uvw(2), uvw(1))

      ! Search for equi-binned angles
      dangle = PI / real(size(polar),8)
      i_pol  = floor(my_pol / dangle + ONE)
      dangle = TWO * PI / real(size(azimuthal),8)
      i_azi  = floor((my_azi + PI) / dangle + ONE)

    end subroutine find_angle

end module mgxs_header
