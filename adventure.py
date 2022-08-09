nama = input("masukan nama kamu : ")
print(f"selamat datang {nama}, mari kita berpetualang!!")

jawaban = input(f"{nama},kamu sedang berada didalam hutan dan menemukan jalan yang bercabang kiri atau kanan? : ").lower()

if jawaban == "kiri":
    jawaban = input(f"ok {nama}, di perjalanan kamu melihat jembatan, apakah kamu ingin melewatinya? ya/tidak : ")
    if jawaban == "ya":
        print(f"jembatan yang kamu lewati rapuh, kamu jatuh kejurang and goodbye {nama} ")
    elif jawaban == "tidak":
        print(f"kamu kehilangan arah lalu tersesat, selamat menikmati hidup di hutan yaaaa {nama}")
    else:
        print("pilihan kamu salah, kamu keluar dari petualangan ini")
elif jawaban == "kanan":
    jawaban = input(f"ok {nama}, kamu bertemu seseorang, apakah ingin menyapa atau di abaikan? sapa/abaikan : ")
    if jawaban == "sapa":
        jawaban = input("ternyata dia tersesat sudah 10 tahun dan memilih untuk tinggal dihutan, lalu kamu di ajak tinggal di hutan juga, ya/tidak : ")
        if jawaban == "ya":
            print(f"selamat {nama}, kamu bahagia hidup bersamanya di dalam hutan!! wkwkwkw")
    elif jawaban == "abaikan":
        print(f"dia melihat kamu dan kamu di anggap ancaman sehingga kamu di bunuh!! goodbye {nama}")
    else:
        print("pilihan kamu salah, kamu keluar dari petualangan ini")
else:
    print("pilihan kamu salah, kamu keluar dari petualangan ini")