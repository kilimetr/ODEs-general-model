# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr

def mixer1(x, t, Caf, Tf):
	Ca = x[0]
	T  = x[0]

	q = 100
	V = 100

	dCadt = q/V * (Caf - Ca)
	dTdt  = q/V * (Tf  - T)

	dydt = [dCadt, dTdt]

	return dydt



def mixer2(x, t, pars):
	Caf = pars[0]
	Tf  = pars[1]

	Ca = x[0]
	T  = x[0]

	q = 100
	V = 100

	dCadt = q/V * (Caf - Ca)
	dTdt  = q/V * (Tf  - T)

	dydt = [dCadt, dTdt]

	return dydt

