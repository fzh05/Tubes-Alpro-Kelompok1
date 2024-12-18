import tkinter as tk
from tkinter import messagebox as msg
import json #JavaScriptObjectNotation (buat  format data yang lebih mudah dibaca)
import os 

# Menyimpan soal berdasarkan mata kuliah
questions = {
    "Alpro": [],
    "ADS": [],
    "LMD": [],
    "ALE": [],
    "Struktur Data": [],
    "Teori Peluang": []
}

# === Fungsi untuk menyimpan pertanyaan ke dalam file json === 
def save_question():
    try:
        with open("pertanyaan.json", "w") as file:
            json.dump(questions, file, indent=4)
        print("Pertanyaan berhasil disimpan ke pertanyaan.json.")
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan pertanyaan: {e}")

def load_question():
    try:
        with open("pertanyaan.json", "r") as file:
            global questions
            questions = json.load(file)
        print("Pertanyaan berhasil dimuat dari pertanyaan.json.")
    except FileNotFoundError:
        print("File pertanyaan.json tidak ditemukan. Memulai dengan daftar kosong.")
    except json.JSONDecodeError:
        print("File pertanyaan.json rusak atau format tidak valid.")
    except Exception as e:
        print(f"Terjadi kesalahan saat memuat pertanyaan: {e}")

# muat pertanyaan saat program dimulai
load_question()

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
    
    # Tombol kecil untuk Hapus dan Edit di pojok kanan bawah
    frame_bottom = tk.Frame(window_main, bg="#081F5C")
    frame_bottom.pack(side="bottom", anchor="se", padx=20, pady=20)

    btn_edit = tk.Button(frame_bottom, text="Edit Soal", command=lambda: edit_question_menu(window_main),
                         font=("Times New Roman", 12), bg="#FFD700", fg="#081F5C", width=10, relief="raised", bd=3)
    btn_edit.grid(row=0, column=0, padx=5)

    btn_delete = tk.Button(frame_bottom, text="Hapus Soal", command=lambda: delete_question_menu(window_main),
                           font=("Times New Roman", 12), bg="#FF4500", fg="white", width=10, relief="raised", bd=3)
    btn_delete.grid(row=0, column=1, padx=5)

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
            save_question #simpan pertanyaan setelah menambahkan
            msg.showinfo("Sukses", f"Soal pilihan berganda untuk {matkul} berhasil ditambahkan!")
            question_window.destroy()
        else:
            msg.showerror("Error", "Semua kolom harus diisi dan jawaban yang benar harus A, B, C, atau D!")

    tk.Button(question_window, text="Simpan", font=("Times New Roman", 16), bg="#F7F2EB", fg="#081F5C", width=10, command=save_question).pack(pady=20)

# === Fungsi Tampilkan Soal ===
def show_matkul_selection(window):
    matkul_window = tk.Toplevel(window)
    matkul_window.title("Pilih Mata Kuliah")
    matkul_window.geometry("400x200")
    matkul_window.config(bg="#081F5C")

    for matkul in questions.keys():
        tk.Button(matkul_window, text=matkul, font=("Times New Roman", 24),
                  bg="#F7F2EB", fg="#081F5C", command=lambda m=matkul: start_quiz(m, matkul_window)).pack(pady=20)

# === Fungsi Hapus Soal ===
def delete_question_menu(window):
    delete_window = tk.Toplevel(window)
    delete_window.title("Hapus Soal")
    delete_window.geometry("400x300")
    delete_window.config(bg="#081F5C")

    for matkul in questions.keys():
        tk.Button(delete_window, text=f"Hapus Soal {matkul}", font=("Times New Roman", 16), 
                  bg="#F7F2EB", fg="#081F5C", command=lambda m=matkul: delete_question(m, delete_window)).pack(pady=10)

def delete_question(matkul, window):
    delete_window = tk.Toplevel(window)
    delete_window.title(f"Hapus Soal {matkul}")
    delete_window.geometry("400x300")
    delete_window.config(bg="#081F5C")

    if not questions[matkul]:
        msg.showerror("Error", f"Tidak ada soal untuk mata kuliah {matkul}")
        delete_window.destroy()
        return

    for i, (author, question) in enumerate(questions[matkul]):
        tk.Button(delete_window, text=f"{i+1}. {question['question'][:30]}...", font=("Times New Roman", 14), 
                  bg="#F7F2EB", fg="#081F5C", command=lambda idx=i: confirm_delete(matkul, idx, delete_window)).pack(pady=5)

def confirm_delete(matkul, idx, delete_window):
    if msg.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus soal ini?"):
        del questions[matkul][idx]
        save_question()
        msg.showinfo("Sukses", "Soal berhasil dihapus.")
        delete_window.destroy()

# === Fungsi Edit Soal ===
def edit_question_menu(window):
    edit_window = tk.Toplevel(window)
    edit_window.title("Edit Soal")
    edit_window.geometry("400x300")
    edit_window.config(bg="#081F5C")

    for matkul in questions.keys():
        tk.Button(edit_window, text=f"Edit Soal {matkul}", font=("Times New Roman", 16),
                  bg="#F7F2EB", fg="#081F5C", command=lambda m=matkul: edit_question(m, edit_window)).pack(pady=10)

def edit_question(matkul, window):
    edit_window = tk.Toplevel(window)
    edit_window.title(f"Edit Soal {matkul}")
    edit_window.geometry("500x400")
    edit_window.config(bg="#081F5C")

    if not questions[matkul]:
        msg.showerror("Error", f"Tidak ada soal untuk mata kuliah {matkul}")
        edit_window.destroy()
        return

    for i, (author, question) in enumerate(questions[matkul]):
        tk.Button(edit_window, text=f"{i+1}. {question['question'][:30]}...", font=("Times New Roman", 14),
                  bg="#F7F2EB", fg="#081F5C",
                  command=lambda idx=i: edit_question_form(matkul, idx, edit_window)).pack(pady=5)

def edit_question_form(matkul, idx, edit_window):
    edit_window.destroy()
    question_window = tk.Toplevel()
    question_window.title(f"Edit Soal untuk {matkul}")
    question_window.geometry("400x400")
    question_window.config(bg="#081F5C")

    question = questions[matkul][idx][1]

    # Input untuk soal
    tk.Label(question_window, text="Soal:", font=("Times New Roman", 14), bg="#081F5C", fg="#F7F2EB").pack(pady=10)
    entry_question = tk.Entry(question_window, font=("Times New Roman", 14), width=30)
    entry_question.insert(0, question['question'])
    entry_question.pack(pady=10)

    # Input untuk pilihan
    options = {}
    for option in ['A', 'B', 'C', 'D']:
        tk.Label(question_window, text=f"Option {option}:", font=("Times New Roman", 14), bg="#081F5C", fg="#F7F2EB").pack(pady=5)
        options[option] = tk.Entry(question_window, font=("Times New Roman", 14), width=30)
        options[option].insert(0, question['options'][option])
        options[option].pack(pady=5)

    # Input untuk jawaban yang benar
    tk.Label(question_window, text="Correct Answer (A/B/C/D):", font=("Times New Roman", 14), bg="#081F5C", fg="#F7F2EB").pack(pady=10)
    entry_correct_answer = tk.Entry(question_window, font=("Times New Roman", 14), width=30)
    entry_correct_answer.insert(0, question['correct_answer'])
    entry_correct_answer.pack(pady=10)

    def save_edit():
        question_text = entry_question.get()
        option_A = options['A'].get()
        option_B = options['B'].get()
        option_C = options['C'].get()
        option_D = options['D'].get()
        correct_answer = entry_correct_answer.get().upper()

        if question_text and option_A and option_B and option_C and option_D and correct_answer in ['A', 'B', 'C', 'D']:
            questions[matkul][idx] = (questions[matkul][idx][0], {
                'question': question_text,
                'options': {'A': option_A, 'B': option_B, 'C': option_C, 'D': option_D},
                'correct_answer': correct_answer
            })
            save_question()
            msg.showinfo("Sukses", "Soal berhasil diedit!")
            question_window.destroy()
        else:
            msg.showerror("Error", "Semua kolom harus diisi dan jawaban yang benar harus A, B, C, atau D!")

    tk.Button(question_window, text="Simpan", font=("Times New Roman", 16), bg="#F7F2EB", fg="#081F5C", width=10, command=save_edit).pack(pady=20)

# === Fungsi untuk memulai kuis ===
def start_quiz(matkul, window):
    # Membuka jendela baru untuk kuis
    quiz_window = tk.Toplevel(window)
    quiz_window.title(f"Kuis {matkul}")
    quiz_window.geometry("600x500")
    quiz_window.config(bg="#081F5C")
    
    # Menampilkan pesan awal
    tk.Label(quiz_window, text="Selamat datang di Kuis Sains Data!",
             font=("Times New Roman", 20, "bold"), bg="#081F5C", fg="white").pack(pady=20)
    
    total_questions = len(questions[matkul])
    correct_answers = [0]  # Menggunakan list untuk membuatnya mutable dalam rekursi

    if total_questions == 0:
        msg.showerror("Error", f"Tidak ada soal untuk mata kuliah {matkul}!")
        quiz_window.destroy()
        return

    # Fungsi untuk memuat pertanyaan menggunakan rekursi
    def load_question(question_index=0):
        # Bersihkan widget sebelumnya
        for widget in quiz_window.winfo_children():
            widget.destroy()

        # Jika indeks melampaui total pertanyaan, tampilkan skor
        if question_index >= total_questions:
            tk.Label(quiz_window, text=f"Skor Anda: {correct_answers[0]}/{total_questions}",
                     font=("Times New Roman", 20, "bold"), bg="#081F5C", fg="white").pack(pady=20)
            # Tambahkan ucapan terima kasih setelah kuis selesai
            tk.Label(quiz_window, text="Terimakasih telah menyelesaikan kuis dengan jujur.",
                     font=("Times New Roman", 16, "italic"), bg="#081F5C", fg="white").pack(pady=20)
            tk.Button(quiz_window, text="Keluar", font=("Times New Roman", 16), bg="#FF4500", fg="white",
                      command=quiz_window.destroy).pack(pady=10)
            return

        # Ambil data pertanyaan
        question_data = questions[matkul][question_index][1]
        
        # Tampilkan pertanyaan dan opsi jawaban
        tk.Label(quiz_window, text=f"Pertanyaan {question_index + 1}/{total_questions}",
                 font=("Times New Roman", 14), bg="#081F5C", fg="#F7F2EB").pack(pady=10)
        tk.Label(quiz_window, text=question_data['question'],
                 font=("Times New Roman", 16, "bold"), bg="#081F5C", fg="#F7F2EB", wraplength=500).pack(pady=10)

        for option, answer_text in question_data['options'].items():
            tk.Button(quiz_window, text=f"{option}: {answer_text}",
                      font=("Times New Roman", 14), bg="#F7F2EB", fg="#081F5C",
                      command=lambda opt=option: check_answer(opt, question_data['correct_answer'], question_index)).pack(pady=5)

    # Fungsi untuk memeriksa jawaban dan lanjut ke pertanyaan berikutnya
    def check_answer(selected_option, correct_option, question_index):
        if selected_option == correct_option:
            correct_answers[0] += 1
        load_question(question_index + 1)

    # Muat pertanyaan pertama
    load_question()

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
