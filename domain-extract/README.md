# Domain extract
All solutions utilize `sort` and `uniq` for removing duplicates.

1st solution has complicated `sed` substitution, that matches base domain as capture group and substitutes everything else with it. First, optional, capture group matches subdomain and protocol, if any and it is discarded. `tr` is used for lowercasing everything.

2nd solution uses sed for removing trailing `.`, if any. Actual filtering is done by reversing input string and selecting two first `.`-delimited fields with `cut` and then reversing input again.

3rd solution removes `/` and `.` -characters and uses `awk` to print second to last and last fields in lower case.

All solutions tested on MacOS 15 (zsh) and Debian 11.6 (bash).