#!/usr/bin/python3
# -*- coding: utf-8  -*-

import csv

csvfile = open('laClasse.csv' )
reader = csv.DictReader(csvfile)

for row in reader:
    print(row['nom'], row['classe'], row['note'], type( row['note'] ) )
    #print(row)

csvfile.close()


classe = [

        [ 'nom', 'classe', 'note'  ],
        [ 'jean', '6eme', 13  ],
        [ 'julie', '6eme', 16  ],
        [ 'bernard', '5eme', 13  ]
]


csvfile = open('laClasse2.csv', 'w' )
writer = csv.writer( csvfile, delimiter=';',  quotechar='"', quoting=csv.QUOTE_NONNUMERIC )
writer.writerows( classe  )
csvfile.close()


