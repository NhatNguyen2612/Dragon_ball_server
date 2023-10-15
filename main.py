import wget, os

logo = f'''

     ██╗██╗███╗   ██╗███╗   ██╗
     ██║██║████╗  ██║████╗  ██║
     ██║██║██╔██╗ ██║██╔██╗ ██║
██   ██║██║██║╚██╗██║██║╚██╗██║
╚█████╔╝██║██║ ╚████║██║ ╚████║
 ╚════╝ ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝
'''

# Hiển thị logo 
print(logo)

print("[1] TẢI DỮ LIỆU\n[2] CHẠY SERVER\n")

# Bắt sự kiện người dùng nhập
# Lưu giá trị của người dùng vào biến "choose"
choose = input("NHẬP: ")

# Lặp và thực hiện các hành động khác nhau dựa trên giá trị của biến
while True:

  if choose == "1":
    # Biến duong_dan_tai_du_lieu sẽ chứa cái liên kết tới tệp của bạn
    duong_dan_tai_du_lieu = "dán đường dẫn của bạn vào đây"
    
    # Sử dụng "wget.download" để tải về
    wget.download(duong_dan_tai_du_lieu)

  elif choose == "2":
    # Chạy Server
    os.system("python run.py")
  else:
    exit()
