
regular expression = $ (a)^{n} (a?)^{n}$
input = $a^n$

| n| re2 | rs-pderiv |
|---|---|---|
|100| | |
|1000| | |
|10000| | 0.031|





```
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