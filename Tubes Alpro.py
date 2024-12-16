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

# === Fungsi Tampilkan Soal ===
def show_matkul_selection(window):
    matkul_window = tk.Toplevel(window)
    matkul_window.title("Pilih Mata Kuliah")
    matkul_window.geometry("400x200")
    matkul_window.config(bg="#081F5C")

    for matkul in questions.keys():
        tk.Button(matkul_window, text=matkul, font=("Times New Roman", 24),
                  bg="#F7F2EB", fg="#081F5C", command=lambda m=matkul: start_quiz(m, matkul_window)).pack(pady=20)

# Fungsi Mulai Kuis
def start_quiz(matkul, window):
    quiz_window = tk.Toplevel(window)
    quiz_window.title(f"Kuis {matkul}")
    quiz_window.geometry("500x400")
    quiz_window.config(bg="#081F5C")
    
    question_index = 0
    correct_answers = 0
    total_questions = len(questions[matkul])
    
    def next_question():
        nonlocal question_index
        if question_index < total_questions:
            question = questions[matkul][question_index][1]
            tk.Label(quiz_window, text=f"{question['question']}", font=("Times New Roman", 16), bg="#081F5C", fg="#F7F2EB").pack(pady=20)
            
            for option, answer in question['options'].items():
                tk.Button(quiz_window, text=f"{option}: {answer}", font=("Times New Roman", 16), 
                          bg="#F7F2EB", fg="#081F5C", command=lambda ans=option: check_answer(ans, question['correct_answer'])).pack(pady=5)
            question_index += 1
        else:
            show_score()

    def check_answer(ans, correct_answer):
        nonlocal correct_answers
        if ans == correct_answer:
            correct_answers += 1
        next_question()

    def show_score():
        score = f"Your score: {correct_answers}/{total_questions}"
        msg.showinfo("Kuis Selesai", score)
        quiz_window.destroy()

    next_question()

# === Program Utama ===
root = tk.Tk()
root.title("Login to Kuis")
root.geometry("400x300")
root.config(bg="#081F5C")

# Input Login
tk.Label(root, text="Username:", font=("Times New Roman", 14), bg="#081F5C", fg="#F7F2EB").pack(pady=10)
entry_username = tk.Entry(root, font=("Times New Roman", 14))
entry_username.pack(pady=10)

tk.Label(root, text="Password:", font=("Times New Roman", 14), bg="#081F5C", fg="#F7F2EB").pack(pady=10)
entry_password = tk.Entry(root, font=("Times New Roman", 14), show="*")
entry_password.pack(pady=10)

tk.Button(root, text="Login", font=("Times New Roman", 16), bg="#F7F2EB", fg="#081F5C", width=10, command=login).pack(pady=20)

root.mainloop()
