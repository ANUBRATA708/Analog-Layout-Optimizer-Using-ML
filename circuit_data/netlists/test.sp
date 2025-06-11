* Simple Op-Amp Netlist
M1 out in1 VDD VDD PMOS L=0.18u W=5u
M2 out in2 VDD VDD PMOS L=0.18u W=5u
M3 in1 in2 0 0 NMOS L=0.18u W=2u
VDD VDD 0 DC 1.8
VIN in1 0 DC 0.9
.END
