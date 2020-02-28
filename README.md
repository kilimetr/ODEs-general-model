# ODEs-general-model

Two options how to write model for ODEs:
	1) In function head all parameters (indenpendent variables = known variables) can be writen and with useage of scipy.integrate's "args" are called by main script packed and imported by "args";
	2) Parameters are packed in vector of parameters called "pars" (by me), (unknown) variables are packed in vector called "yvec". 
		Function has three positions in head:
			1. Integrated variable created by linspace (time, dimension, volume, ...);
			2. Parameters of the function "pars";
			3. Integrated dependent variables "yvec".
		Those three "packages" are replaced by anonymous function "lambda" in main script.

License: For sharing and useage or other operations with my code/codes my approval is needed - contact me via email or linkedin (find info in my profile)!