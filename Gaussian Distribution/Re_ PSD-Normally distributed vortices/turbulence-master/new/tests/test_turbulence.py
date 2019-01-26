"""
Just testing whether an example executes without generating exceptions...
"""

import numpy as np

from turbulence import Gaussian2DTempWind, VonKarman2DTempWind, Comparison, Field2D
   
def test_some():
    """Given parameters."""
    N = 20                     # Amount of modes
    k_max = 10.0                # Maxmimum wavenumber
    
    """Parameters for Gaussian spectrum."""
    a = 1.0                     # Correlation length
    sigma_T = np.sqrt(1e-5)     # Standard deviation in temperature
    T_0 = 1.0                   # Temperature
    sigma_nu = 0.0              # Standard deviation in wind
    
    
    """Parameters for Von Karman spectrum."""
    K_0 = 1.0/10.0
    L = 2.0 * np.pi / K_0       # Size of largest eddy.
    C_T = np.sqrt(1e-7)         # 
    T_0 = 1.0                   #
    C_v = 0.001
    c_0 = 1.0
    
    
    """Other settings."""
    wavenumber_resolution = k_max / N
    spatial_resolution = 0.05   # We don't need it for the calculations but we do need it to create an instance.
    
    x = 20.0
    y = 0.0
    z = 40.0
    
    plane=(1,0,1)
    
    
    g = Gaussian2DTempWind(max_mode_order=N,
                        a=a,
                        sigma_T=sigma_T,
                        T_0=T_0,
                        sigma_nu=sigma_nu,
                        c_0=c_0,
                        wavenumber_resolution=wavenumber_resolution,
                        plane=plane
                        )
    
    vk = VonKarman2DTempWind(max_mode_order=N, 
                            L=L,
                            C_T=C_T,
                            T_0=T_0,
                            C_v=C_v,
                            c_0=c_0,
                            wavenumber_resolution=wavenumber_resolution,
                            plane=plane
                            )
    
    field_g = Field2D(x=x, y=y, z=z, spectrum=g, spatial_resolution=spatial_resolution)
    field_vk = Field2D(x=x, y=y, z=z, spectrum=vk, spatial_resolution=spatial_resolution)
    c = Comparison([g, vk])
    
    field_g.generate()
    field_vk.generate()
    

    
