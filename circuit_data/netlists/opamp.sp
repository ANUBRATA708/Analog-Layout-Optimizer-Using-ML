* Two-stage Op-Amp Netlist
M1 out in1 VDD VDD PMOS L=0.18u W=5u
M2 out in2 VDD VDD PMOS L=0.18u W=5u
M3 in1 in2 0 0 NMOS L=0.18u W=2u
M4 in2 in1 0 0 NMOS L=0.18u W=2u
R1 out VDD 1k
C1 out 0 2p
.END
