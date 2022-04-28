from time import time # untuk merekam waktunya


# menghitung akurasi kecepatan ketikan
def tperror(prompt):
    global inwords

    words = prompt.split()
    errors = 0

    for i in range(len(inwords)):
        if i in (0, len(inwords)-1):
            if inwords[i] == words[i]:
                continue
            else:
                errors = errors + 1
        else:
            if inwords[i] == words[i]:
                if(inwords[i+1]==words[i+1]) & (inwords[i+1]==words[i+1]):
                    continue
                else:
                    errors += 1
            else:
                errors += 1
    return errors

# menghitung kecepatan ketikan

def speed(inpromt, stime, etime):
    global time
    global inwords

    inwords = inpromt.split()
    twords = len(inwords)
    speed = twords / time

    return speed

# menghitung total gabungan keduanya

def elapsedtime(stime, etime):
    time = stime + etime
    return time

if __name__ == '__main__':
    prompt = "python in an interpreted, high-level, general-surpose programming language.created by Guido van rossum and first released in 1991"
    # ini paragrap yang akan di ketik
    print("type this:- ",prompt, " ")

    # check input ketikan
    input("tekan Enter kalau ente sudah siap check kecepatan ngetiknya")

    # merekan time untuk inputan
    stime = time()
    inpromt = input()
    etime = time()

    # mengambil semua informasi yang di return masing2 fungsi
    time = round(elapsedtime(stime,etime),2)
    speed = speed(inpromt,stime,etime)
    errors = tperror(prompt)

    # print semua yang di butuhkan untuk melihat hasilnya
    print("x"* 50)
    print("total time elapsed:", time, "detik")
    print("nilai rata-rata kecepatan mengetik anda", speed, "kata per menit (w/m)")
    print("dengan total error", errors, "errors")
    print("x"* 50)