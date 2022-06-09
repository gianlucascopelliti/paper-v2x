# Tv evaluation

## PRL size

Computed according to Scenario 2 with 20% share of attackers in the network (`p =
0.000196612735153`)

Percentiles and values:

```
e = [30, 150, 300, 900]

0.5: (6, 24, 45, 121)
0.75: (7, 27, 50, 128)
0.9: (9, 30, 54, 134)
0.99: (11, 36, 61, 145)
0.9999: (16, 43, 71, 160)
```

With a more realistic scenario, i.e., Scenario 1 with 1% attackers (`p =
0.000007813830433`):

```
0.5: (1, 2, 3, 6)
0.75: (1, 2, 4, 8)
0.9: (2, 3, 5, 10)
0.99: (3, 5, 7, 13)
0.9999: (4, 7, 10, 17)
```

Check the readme in `v2x-revocation-proof` for more info.