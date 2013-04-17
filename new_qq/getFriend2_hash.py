'''
function (a, e) {
                for (var c = [], d = 0; d < a.length; d++) c[d] = a.charAt(d) - 0;
                for (var b = 0, k = -1, d = 0; d < c.length; d++) {
                    b += c[d];
                    b %= e.length;
                    var f = 0;
                    if (b + 4 > e.length) for (var g = 4 + b - e.length, h = 0; h < 4; h++) f |= h < g ? (e.charCodeAt(b + h) & 255) << (3 - h) * 8 : (e.charCodeAt(h - g) & 255) << (3 - h) * 8;
                    else for (h = 0; h < 4; h++) f |= (e.charCodeAt(b + h) & 255) << (3 - h) * 8;
                    k ^= f
                }
                c = [];
                c[0] = k >> 24 & 255;
                c[1] = k >> 16 & 255;
                c[2] = k >> 8 & 255;
                c[3] = k & 255;
                k = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"];
                d = "";
                for (b = 0; b < c.length; b++) d += k[c[b] >> 4 & 15], d += k[c[b] & 15];
                return d
            }
'''

def getFriend2_hash(a, e):
    c = [int(i) for i in a]
    b = 0
    k = -1
    for d in xrange(len(c)):
        b += c[d]
        b %= len(e)
        f = 0
        if b + 4 > len(e):
            g = 4 + b - len(e)
            for h in xrange(4):
                f |= (ord(e[b + h]) & 255) << (3 - h) * 8 if h < g else (ord(e[h - g]) & 255) << (3 - h) * 8
        else:
            for h in xrange(4):
                f |= (ord(e[b + h]) & 255) << (3 - h) * 8
        k ^= f

    c = [0 for i in xrange(4)]
    c[0] = k >> 24 & 255
    c[1] = k >> 16 & 255
    c[2] = k >> 8 & 255
    c[3] = k & 255
    k = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    d = ""
    for b in xrange(len(c)):
        d += k[c[b] >> 4 & 15]
        d += k[c[b] & 15]
    return d

if __name__ == "__main__":
    print getFriend2_hash('2596600470', 'eb0a52bb7e2145ae9bf4b8ccdcee4d384e6952887524430a1b4917f1b09ae5b3')
