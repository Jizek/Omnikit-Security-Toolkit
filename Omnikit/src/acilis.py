import os
import random
srum = open("surum.txt")
surum = srum.read()
os.system("cls" if os.name == "nt" else "clear")
r1 = ("\033[91m")
r2 = ("\033[92m")
r3 = ("\033[93m")
r4 = ("\033[94m")
r5 = ("\033[95m")
r6 = ("\033[96m")
reng = [r1,r2,r3,r4,r5,r6]
renkk = random.choice(reng)
print(renkk)

# Omnikit ASCII Art Banner
print("""
 ██████╗ ███╗   ███╗███╗   ██╗██╗██╗  ██╗██╗████████╗
██╔═══██╗████╗ ████║████╗  ██║██║██║ ██╔╝██║╚══██╔══╝
██║   ██║██╔████╔██║██╔██╗ ██║██║█████╔╝ ██║   ██║   
██║   ██║██║╚██╔╝██║██║╚██╗██║██║██╔═██╗ ██║   ██║   
╚██████╔╝██║ ╚═╝ ██║██║ ╚████║██║██║  ██╗██║   ██║   
 ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝╚═╝   ╚═╝   
                                                       
        Security Toolkit v""" + surum + """
        Geliştirici: jizek
        github.com/jizek/omnikit
""")

print("""
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║  Bu araçla gerçekleştireceğiniz tüm işlemlerin          ║
║  sorumluluğu tamamen size aittir.                       ║
║                                                           ║
║  Geliştirici hiçbir hukuki veya etik yükümlülük         ║
║  kabul etmez.                                            ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
""")
