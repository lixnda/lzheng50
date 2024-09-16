"""
Linda Zheng
Boas
SoftDev
K<04> -- <Random Number Generation>
2024-09-13
time spent: 0.2
"""

import random
krewes = {
           4: [
        'DUA','TAWAB','EVA','JACK','VICTOR','EVAN','JASON','COLYI','IVAN','TANZEEM',
        'TAHMIM','STANLEY','LEON','NAOMI','NIA','ANASTASIA','JADY','BRIAN','JACOB',
        'ALEX','CHONGTIAN','DANNY','MARCO','ABIDUR','ANKITA','ANDY','ETHAN','AMANDA',
        'AIDAN','LINDA','QIANJUN','JIAYING','KISHI'
        ],
        5: [ 
            'ADITYA','MARGIE','RACHEL','ALEXANDER','ZIYAD','DANNY','ENDRIT','CADEN',
            'VEDANT','SUHANA','KYLE','KEVIN','RAYMOND','CHRISTOPHER','JONATHAN','SASHA',
            'NAFIYU','TIM','WILL','DANIEL','BENJAMIN','CLAIRE','CHLOE','STELLA','TRACY',
            'JESSICA','JACKIE','WEN YUAN','YINWEI','TIFFANY','JAYDEN DANIEL','PRINCEDEN'
        ]
    }

#random choice only works with list, hence why the dict was converted
print(random.choice(list(random.choice(list(krewes.values())))))