class isotope(object):
    """
    An isotope. Each isotope has the following properties:
    
    Attributes:
        isotope : The name of the isotope, in form 235U
        sigma : The microscopic cross section in cm^2
        rho : Density in g/cm^3
        A : atomic number
    """
    
    def __init__(self, isotope, sigma, rho, A):
        self.isotope = isotope
        self.sigma = sigma
        self.rho = rho
        self.A = A
        
    def Macroscopic_cross_section(self)
        N_A = 6.02*10**23
        self.Sigma = self.sigma * self.rho * N_A / self.A
