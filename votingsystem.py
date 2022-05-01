# tentukan dulu nominasinya
nominasi1 = input("masukan nama yang di pilih: ")
nominasi2 = input("masukan nama yang di pilih: ")

# initial vote count untuk keduanya harus 0
nm1_votes = 0
nm2_votes = 0

voter_id = [1,2,3,4,5,6,7,8,9,10]

no_voter = len(voter_id)

while True:
    if voter_id == []: # check ketika vote selesai
        print("sesi voting selesai!!!")
        if nm1_votes>nm2_votes:
            percent=(nm1_votes/no_voter)*100
            print(nominasi1, "memenangkan pemilihan dengan ", percent,"% of votes" )
            break
        elif nm2_votes>nm1_votes:
            percent=(nm2_votes/no_voter)*100
            print(nominasi2, "memenangkan pemilihan dengan ", percent,"% of votes ")
            break
        else:
            print("keduanya memiliki suara yang sama, vote di ulang")
            break




    voter = int(input("masukan id voter : "))
    if voter in voter_id:
        print("you are a voter")
        voter_id.remove(voter)
        print("-"*50)
        print("vote untuk", nominasi1, "tekan 1 ")
        print("vote untuk", nominasi2, "tekan 2 ")
        print("-"*50)
        vote = int(input("masukan vote : "))
        if vote == 1:
            nm1_votes +=1
            print(nominasi1, "trims partisipasinya")
        elif vote == 2:
            nm2_votes += 1
            print(nominasi2, "trims partisipasinya")
        elif vote > 2:
            print("perhatikan voting ente")
        else:
            print("ente golput")
