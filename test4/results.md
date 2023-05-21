
regular expression = $ (a)^{n} (a?)^{n}$
input = $a^n$

| n| re2 | rs-pderiv |
|---|---|---|
|100| 0.003 | 0.014 |
|1000| 0.25 | 0.015 |
|10000| 28 | 0.031|

pyre2

```

$ python3 testre2.py 10000 ~/git/regex-pderiv/benchmarks/bitc/input10000.txt
a
0:00:28.507025
```



```
Ok(
    14.565983ms,
)
./target/release/rs-pderiv 100 ~/git/regex-pderiv/benchmarks/bitc/input100.txt   0.06s  user 0.00s system 79% cpu 0.075 total
avg shared (code):         0 KB
avg unshared (data/stack): 0 KB
total (sum):               0 KB
max memory:                3 MB
page faults from disk:     0
other page faults:         549


Ok(
    15.656243ms,
)
./target/release/rs-pderiv 1000    45.69s  user 0.06s system 99% cpu 45.771 total
avg shared (code):         0 KB
avg unshared (data/stack): 0 KB
total (sum):               0 KB
max memory:                164 MB
page faults from disk:     0
other page faults:         41810


Ok(
    31.396636ms,
)
./target/release/rs-pderiv 10000    44594.02s  user 62.24s system 99% cpu 12:24:20.68 total
avg shared (code):         0 KB
avg unshared (data/stack): 0 KB
total (sum):               0 KB
max memory:                62043 MB
page faults from disk:     7379804
other page faults:         25105965
```