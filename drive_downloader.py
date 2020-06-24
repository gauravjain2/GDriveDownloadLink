print("Welcome to Drive Download Link Generator")
while(1):
    try:
        downloadLink = (((input('\n Please paste in your URL: ').replace('file/d/', 'uc?export=download&id=')).replace('/view?usp=sharing', '')).replace('/view', ''))
        print('\n || Your URL is: ', downloadLink)
    except:
        print("Some Error Occurred, Check the link and try again!")
    ch=int(input("\nWanna Do again? press 1 for yes , 2 for no"))
    if(ch!=1):
        exit()