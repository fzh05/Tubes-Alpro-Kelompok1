import tkinter as tk
from tkinter import messagebox as msg

# Menyimpan soal berdasarkan mata kuliah
questions = {
    "Alpro": [],
    "ADS": [],
    "LMD": [],
    "ALE": [],
    "Struktur Data": [],
    "Teori Peluang": []
}

# === Fungsi Menu ===
def about_me():
    msg.showinfo("About Me", 
                 "Hallo!\n\n"
                 "Kami dari kelompok 1 RC\n"
                 "Program ini dibuat untuk tugas besar mata kuliah Algoritma Pemrograman.\n"
                 "Anggota kelompok :\n"
                 "Sania Dwi Ayu Lestari\n"
                 "Afifah Fauziah\n"
                 "Aprilia Dewi Hutapea\n"
                 "Muhammad Naufal Alghani\n"
                 "Selamat mencoba program quiz kami!")

def send_feedback():
    tanya = msg.askquestion('Feedback', 'Was your experience good with us?')
    if tanya == 'yes':
        msg.showinfo('Feedback', "Nice to know your good experience! :) \n"
                                 "Please Like my video and share your experience in the Comment (<3)")
    else:
        msg.showwarning('Feedback', "Oh, sorry to hear that. Feel free to contact us to share your feedback!")

def exit_app():
    if msg.askyesno("Exit", "Are you sure you want to exit?"):
        root.quit()

# === Fungsi Login ===
def login():
    username = entry_username.get()
    password = entry_password.get()

    if username and len(username) <= 50 and password:
        root.destroy()
        main_window(username)
    elif len(username) > 50:
        msg.showerror("Login Error", "Username must not exceed 50 characters!")
    else:
        msg.showerror("Login Error", "Username or password cannot be empty!")

# === Fungsi Main Window ===
def main_window(username):
    window_main = tk.Tk()
    window_main.title("Aplikasi Kuis")
    window_main.geometry("1000x600")
    window_main.config(bg="#081F5C")  

    # Tombol Buat Soal
    tk.Button(window_main, text="Buat Soal Quiz",
              command=lambda: add_question(window_main, username), 
              font=("Times New Roman", 21), bg="#F7F2EB", fg="#081F5C",
              width=14, height=2, relief="raised", bd=8).pack(pady=20)

    # Tombol Lihat Soal
    tk.Button(window_main, text="Start Quiz",
              command=lambda: show_matkul_selection(window_main), 
              font=("Times New Roman", 21), bg="#F7F2EB", fg="#081F5C",
              width=14, height=2, relief="raised", bd=8).pack(pady=20)

    # Tombol Logout
    tk.Button(window_main, text="Logout",
              command=window_main.quit, 
              font=("Times New Roman", 21), bg="#F7F2EB", fg="#081F5C",
              width=14, height=2, relief="raised", bd=8).pack(pady=20)

    window_main.mainloop()

# === Fungsi Tambah Soal ===
def add_question(window, username):
    add_window = tk.Toplevel(window)
    add_window.title("Tambah Soal")
    add_window.geometry("400x200")
    add_window.config(bg="#081F5C")

    matkul_options = list(questions.keys())

    # Membuat tombol untuk setiap mata kuliah
    for matkul in matkul_options:
        tk.Button(add_window, text=matkul, font=("Times New Roman", 16),
                  bg="#F7F2EB", fg="#081F5C", width=14, height=1,
                  command=lambda m=matkul: show_add_question_form(m, add_window, username)).pack(pady=20)

# Fungsi untuk Menampilkan Formulir Soal Pilihan Berganda
def show_add_question_form(matkul, add_window, username):
    add_window.destroy()  # Menutup jendela pilih mata kuliah

    # Menampilkan form untuk menambahkan soal
    question_window = tk.Toplevel()
    question_window.title(f"Tambah Soal untuk {matkul}")
    question_window.geometry("400x350")
    question_window.config(bg="#081F5C")

    # Input untuk soal
    tk.Label(question_window, text="Soal:", font=("Times New Roman", 14), bg="#081F5C", fg="#F7F2EB").pack(pady=10)
    entry_question = tk.Entry(question_window, font=("Times New Roman", 14), width=30)
    entry_question.pack(pady=10)

    # Input untuk pilihan
    options = {}
    for option in ['A', 'B', 'C', 'D']:
        tk.Label(question_window, text=f"Option {option}:", font=("Times New Roman", 14), bg="#081F5C", fg="#F7F2EB").pack(pady=5)
        options[option] = tk.Entry(question_window, font=("Times New Roman", 14), width=30)
        options[option].pack(pady=5)

    # Input untuk jawaban yang benar
    tk.Label(question_window, text="Correct Answer (A/B/C/D):", font=("Times New Roman", 14), bg="#081F5C", fg="#F7F2EB").pack(pady=10)
    entry_correct_answer = tk.Entry(question_window, font=("Times New Roman", 14), width=30)
    entry_correct_answer.pack(pady=10)

    def save_question():
        question_text = entry_question.get()
        option_A = options['A'].get()
        option_B = options['B'].get()
        option_C = options['C'].get()
        option_D = options['D'].get()
        correct_answer = entry_correct_answer.get().upper()

        # Validasi input
        if question_text and option_A and option_B and option_C and option_D and correct_answer in ['A', 'B', 'C', 'D']:
            question = {
                'question': question_text,
                'options': {'A': option_A, 'B': option_B, 'C': option_C, 'D': option_D},
                'correct_answer': correct_answer
            }
            questions[matkul].append((username, question))
            msg.showinfo("Sukses", f"Soal pilihan berganda untuk {matkul} berhasil ditambahkan!")
            question_window.destroy()
        else:
            msg.showerror("Error", "Semua kolom harus diisi dan jawaban yang benar harus A, B, C, atau D!")

    tk.Button(question_window, text="Simpan", font=("Times New Roman", 16), bg="#F7F2EB", fg="#081F5C", width=10, command=save_question).pack(pady=20)

# === Fungsi Simpan Soal ===
def assign_question_to_matkul(username, matkul, add_window):
    add_window.destroy()
    question_window = tk.Toplevel()
    question_window.title(f"Tambah Soal untuk {matkul}")
    question_window.geometry("400x200")
    question_window.config(bg="#081F5C")

    # Input Soal
    tk.Label(question_window, text="Soal:", font=("Times New Roman", 18),
             bg="#081F5C", fg="#F7F2EB").pack(pady=40)
    entry_question = tk.Entry(question_window, font=("Times New Roman", 14), width=30)
    entry_question.pack(pady=10)

    def save_question():
        question = entry_question.get()
        if question:
            questions[matkul].append((username, question))
            msg.showinfo("Sukses", f"Soal untuk {matkul} berhasil ditambahkan!")
            question_window.destroy()
        else:
            msg.showerror("Error", "Soal tidak boleh kosong!")

    tk.Button(question_window, text="Simpan",
              font=("Times New Roman", 16), bg="#F7F2EB", fg="#081F5C", width=10,
              command=lambda: save_question(entry_question, matkul, username, question_window)).pack(pady=10)

# === Fungsi Tampilkan Soal ===
def show_matkul_selection(window):
    matkul_window = tk.Toplevel(window)
    matkul_window.title("Pilih Mata Kuliah")
    matkul_window.geometry("400x200")
    matkul_window.config(bg="#081F5C")

    for matkul in questions.keys():
        tk.Button(matkul_window, text=matkul, font=("Times New Roman", 24),
                  bg="#F7F2EB", fg="#081F5C", command=lambda m=matkul: display_questions(m)).pack(pady=20)

def show_add_question_button(matkul, window):
    # Tombol untuk menambah soal akan muncul setelah memilih mata kuliah
    tk.Button(window, text="Tambah Soal", font=("Times New Roman", 18),
              bg="#F7F2EB", fg="#081F5C", command=lambda: add_question(window, matkul)).pack(pady=20)

def display_questions(matkul):
    question_window = tk.Toplevel()
    question_window.title(f"Soal {matkul}")
    question_window.geometry("400x200")
    question_window.config(bg="#081F5C")

    if questions[matkul]:
        for idx, q in enumerate(questions[matkul]):
            tk.Label(question_window, text=f"{idx+1}. {q[1]} (oleh {q[0]})",
                     bg="#081F5C", fg="#F7F2EB", font=("Times New Roman", 18)).pack(pady=10)
    else:
        msg.showinfo("Kosong", f"Tidak ada soal di {matkul}.")
# === Fungsi Tampilkan Soal dengan Opsi Hapus ===
def display_questions(matkul):
    question_window = tk.Toplevel()
    question_window.title(f"Soal {matkul}")
    question_window.geometry("500x400")
    question_window.config(bg="#081F5C")

    if questions[matkul]:
        for idx, q in enumerate(questions[matkul]):
            # Frame untuk setiap soal
            frame = tk.Frame(question_window, bg="#F7F2EB", bd=2, relief="ridge")
            frame.pack(pady=10, padx=10, fill="x")
            
            # Label soal
            tk.Label(frame, text=f"{idx+1}. {q[1]} (oleh {q[0]})", 
                     font=("Times New Roman", 16), bg="#F7F2EB").pack(side="left", padx=10, pady=5)
            
            # Tombol Hapus Soal
            tk.Button(frame, text="Hapus", font=("Times New Roman", 12, "bold"),
                      bg="#FF5C5C", fg="white", relief="raised",
                      command=lambda i=idx: delete_question(matkul, i, question_window)).pack(side="right", padx=10)
    else:
        tk.Label(question_window, text=f"Tidak ada soal di {matkul}.", 
                 font=("Times New Roman", 18), bg="#081F5C", fg="#F7F2EB").pack(pady=20)

# === Fungsi Hapus Soal ===
def delete_question(matkul, index, window):
    confirm = msg.askyesno("Konfirmasi Hapus", "Apakah Anda yakin ingin menghapus soal ini?")
    if confirm:
        del questions[matkul][index]
        msg.showinfo("Sukses", "Soal berhasil dihapus!")
        window.destroy()  # Tutup window lama
        display_questions(matkul)  # Tampilkan ulang daftar soal

# Jendela Login
root = tk.Tk()
root.title("QUIZ BY KELOMPOK 1 RC")
root.geometry("1000x600")
root.configure(bg="#081F5C")

frame_login = tk.Frame(root, bg="#F7F2EB", bd=5, relief="ridge")
frame_login.place(relx=0.5, rely=0.5, anchor="center")

# Judul LOGIN
tk.Label(frame_login, text="LOGIN", font=("Times New Roman", 36, "bold"), bg="#F7F2EB").pack(pady=(10, 20))

# Label Username
tk.Label(frame_login, text="Username:", font=("Times New Roman", 18), bg="#F7F2EB").pack(anchor="w", padx=20)
entry_username = tk.Entry(frame_login, font=("Times New Roman", 18), width=25, relief="solid", bd=2)
entry_username.pack(padx=20, pady=(0, 10))

# Label Password
tk.Label(frame_login, text="Password:", font=("Times New Roman", 18), bg="#F7F2EB").pack(anchor="w", padx=20)
entry_password = tk.Entry(frame_login, font=("Times New Roman", 18), width=25, show="*", relief="solid", bd=2)
entry_password.pack(padx=20, pady=(0, 20))

# Tombol LOGIN
tk.Button(frame_login, text="LOGIN", command=login,
          font=("Times New Roman", 20, "bold"), bg="#081F5C", fg="white",
          width=12, height=1, relief="raised", bd=5).pack(pady=(10, 20))

# Menu Bar
menubar = tk.Menu(root)
root.config(menu=menubar)
menu_file = tk.Menu(menubar, tearoff=0)
menu_file.add_command(label="About", command=about_me)
menu_file.add_command(label="Send Feedback", command=send_feedback)
menu_file.add_separator()
menu_file.add_command(label="Exit", command=exit_app)
menubar.add_cascade(label="Menu", menu=menu_file)

root.mainloop()

