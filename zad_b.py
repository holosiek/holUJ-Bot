import math
B_TESTS = [
    "20 3 50 44 49 23 86 68 67 61 66 3 29 83 34 74 62 64 53 37 99 19 1.9069 2.9858 0.0648 2.6437 1.3173 1.1936 2.8956 2.1533 0.6254 3.2106 0.278 3.0411 2.3006 2.0722 0.3068 1.3951 1.1967 3.2409 1.7771 5 0 11 r",
    "20 49 43 50 53 79 48 12 31 62 23 60 28 25 8 17 26 84 77 30 35 19 2.7598 0.67 1.3325 1.2398 2.9295 0.19 3.0246 0.9432 2.3636 0.3738 1.7225 0.0419 1.3456 0.2122 2.5677 1.3471 0.6344 0.9822 2.5369 0 10 15 m",
    "20 24 12 42 54 38 59 62 40 13 90 58 41 99 26 17 86 6 73 69 14 5 0.08 0.3 0.0826667 0.3 0.237333 5 17 3 w",
    "50 282 98 158 234 68 84 165 26 184 282 221 228 132 291 98 225 194 157 156 91 280 225 29 2 294 245 38 23 198 117 251 183 201 227 154 296 88 8 80 232 173 188 150 183 110 115 61 43 86 117 7 0.0857143 0.117551 0.117613 0.16493 0.213022 0.103258 0.197911 12 33 29 w",
    "20 278 96 75 279 50 59 36 91 119 206 90 183 241 196 254 210 251 165 244 248 13 0.202564 0.134951 0.0764406 0.0736312 0.0446719 0.0227874 0.0296636 0.0191673 0.0934444 0.0589835 0.0374916 0.0190342 0.187169 0 0 9 w",
    "45 295 270 170 181 220 215 114 261 148 278 51 35 262 25 6 200 241 63 128 20 202 81 192 228 35 112 44 74 136 280 249 0 103 133 159 275 75 164 248 297 192 208 149 206 267 7 8.98 0.72 9.12 3 1.35 3.64 3.51 13 33 28 m",
    "44 95 152 143 53 131 191 207 23 83 279 235 182 115 16 171 111 247 181 283 200 141 276 19 226 192 298 97 158 70 112 169 277 225 202 278 160 273 271 207 33 253 165 249 24 15 0.211111 0.0262963 0.137267 0.10839 0.0781148 0.037056 0.0589256 0.00609493 0.067349 0.0107758 0.0155172 0.0475401 0.0425892 0 0.152973 2 1 28 w",
    "57 173 292 167 91 107 101 151 180 247 114 91 279 83 5 105 268 57 292 151 43 159 57 49 180 193 289 20 179 253 90 152 270 55 235 32 232 224 164 236 130 185 89 207 211 144 143 274 274 2 51 48 190 81 141 0 77 51 13 8.85 0.78 5.68 5.06 7.72 5.91 8.29 7.86 4.27 6.44 2.05 9.12 3.4 13 52 42 m",
    "26 226 135 296 153 273 295 17 201 50 207 275 66 42 10 87 66 15 150 223 174 224 113 42 186 289 121 5 0.3 0.3 0.112 0.11712 0.17088 3 15 10 w",
    "23 203 244 76 38 199 278 227 82 256 276 250 95 265 108 239 271 211 29 227 296 37 296 36 3 6.72 5.32 4.47 6 4 13 r"
]

def main(msg, moreInfo=False):
    PREPARE = ""
    numbers = []
    output = []
    xd = []
    mask = []
    splitter = []
    num_size = 0
    mask_size = 0
    separator = 0
    first_index = 0
    last_index = 0
    letsmove = 0
    typee = ''
    pos = 0

    PREPARE += "Input:\n```\n"
    num_size = int(msg[pos])
    PREPARE += msg[pos] + "\n"
    numbers = [0]*num_size
    output = [0]*num_size
    xd = [0]*num_size
    pos += 1
    for i in range(num_size):
        temp = int(msg[pos])
        PREPARE += msg[pos] + " "
        pos += 1
        numbers[i] = temp
        output[i] = temp
    mask_size = int(msg[pos])
    PREPARE += "\n" + msg[pos] + "\n"
    splitter = [0]*mask_size
    mask = [0]*mask_size
    pos += 1
    for i in range(mask_size):
        splitter[i] = float(msg[pos])
        PREPARE += msg[pos] + " "
        pos += 1
    separator = int(msg[pos])
    first_index = int(msg[pos+1])
    last_index = int(msg[pos+2])
    typee = msg[pos+3]
    PREPARE += "\n" + msg[pos] + " " + msg[pos+1] + " " + msg[pos+2] + "\n" + msg[pos+3] + "\n\n"
    pos += 4

    if(first_index > last_index):
        for o in range(first_index, num_size):
            xd[letsmove] = numbers[o]
            letsmove += 1
        for o in range(last_index+1):
            xd[letsmove] = numbers[o]
            letsmove += 1
    else:
        for o in range(first_index,last_index+1):
            xd[letsmove] = numbers[o]
            letsmove += 1

    SKIPPER = first_index

    if(moreInfo):
        PREPARE += "```\nMasks:\n```\n"
    for i in range(letsmove):
        iter = 0
        indx = int(i-(mask_size//2)*(separator+1))
        while(indx < 0):
            indx += letsmove
        while(indx >= letsmove):
            indx -= letsmove
        maskowanie = []
        for j in range(mask_size):
            mask[iter] = xd[indx%letsmove]
            maskowanie.append(xd[indx%letsmove])
            indx += separator+1
            while(indx >= letsmove):
                indx -= letsmove
            while(indx < 0):
                indx += letsmove
            iter += 1
        if(moreInfo):
            PREPARE += str(maskowanie) + "\n"
        if(typee == 'r'):
            sum = 0
            for x in range(mask_size):
                sum += mask[x]
            sum /= mask_size
            output[SKIPPER] = math.floor(sum*100)/100
        elif(typee == 'm'):
            for x in range(mask_size-1):
                for z in range(mask_size-1, x, -1):
                    if(mask[z] > mask[z-1]):
                        temp = mask[z]
                        mask[z] = mask[z-1]
                        mask[z-1] = temp
            output[SKIPPER] = mask[int(mask_size//2)]
        elif(typee == 'w'):
            sum = 0
            for x in range(mask_size):
                sum += mask[x]*splitter[x]
            output[SKIPPER] = math.floor(sum*100)/100
        SKIPPER += 1
        if(SKIPPER >= num_size):
            SKIPPER = 0

    PREPARE += "```\nResult:\n```\n"
    PREPARE += " ".join([str(i) for i in output])
    return PREPARE + "```"

#print(main("20 49 43 50 53 79 48 12 31 62 23 60 28 25 8 17 26 84 77 30 35 19 2.7598 0.67 1.3325 1.2398 2.9295 0.19 3.0246 0.9432 2.3636 0.3738 1.7225 0.0419 1.3456 0.2122 2.5677 1.3471 0.6344 0.9822 2.5369 0 10 15 m".split(" ")))