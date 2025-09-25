import tkinter as tk
from tkinter import messagebox, ttk
import json
from datetime import datetime

# Arquivos para armazenar os dados
task_file = "tasks.json"
shopping_file = "shopping.json"

def load_data(file):
    try:
        with open(file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_data(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

def add_task():
    task = entry_task.get()
    if not task:
        messagebox.showerror("Erro", "A tarefa não pode estar vazia.")
        return

    tasks = load_data(task_file)
    today = datetime.now().strftime("%Y-%m-%d")

    if today not in tasks:
        tasks[today] = {"pending": [], "completed": []}

    tasks[today]["pending"].append(task)
    save_data(task_file, tasks)
    update_task_table()
    entry_task.delete(0, tk.END)

def complete_task():
    selected = task_table.selection()
    if not selected:
        messagebox.showerror("Erro", "Selecione uma tarefa para marcar como concluída.")
        return

    tasks = load_data(task_file)
    today = datetime.now().strftime("%Y-%m-%d")
    for item in selected:
        task = task_table.item(item, "values")[0]
        tasks[today]["pending"].remove(task)
        tasks[today]["completed"].append(task)

    save_data(task_file, tasks)
    update_task_table()

def update_task_table():
    for row in task_table.get_children():
        task_table.delete(row)

    tasks = load_data(task_file)
    today = datetime.now().strftime("%Y-%m-%d")

    if today in tasks:
        for task in tasks[today]["pending"]:
            task_table.insert("", tk.END, values=(task,))

def show_history():
    tasks = load_data(task_file)
    history_window = tk.Toplevel(root)
    history_window.title("Histórico de Tarefas")

    tree = ttk.Treeview(history_window, columns=("Data", "Tarefa"), show="headings")
    tree.heading("Data", text="Data")
    tree.heading("Tarefa", text="Tarefa")
    tree.pack(fill=tk.BOTH, expand=True)

    for date, data in tasks.items():
        for task in data["completed"]:
            tree.insert("", tk.END, values=(date, task))

def add_shopping_item():
    item = entry_item.get()
    if not item:
        messagebox.showerror("Erro", "O item não pode estar vazio.")
        return

    shopping = load_data(shopping_file)
    if "pending" not in shopping:
        shopping["pending"] = []
    shopping["pending"].append(item)
    save_data(shopping_file, shopping)
    update_shopping_table()
    entry_item.delete(0, tk.END)

def complete_shopping_item():
    selected = shopping_table.selection()
    if not selected:
        messagebox.showerror("Erro", "Selecione um item para marcar como comprado.")
        return

    shopping = load_data(shopping_file)
    if "completed" not in shopping:
        shopping["completed"] = []

    for item in selected:
        shopping_item = shopping_table.item(item, "values")[0]
        shopping["pending"].remove(shopping_item)
        shopping["completed"].append(shopping_item)

    save_data(shopping_file, shopping)
    update_shopping_table()

def remove_shopping_item():
    selected = shopping_table.selection()
    if not selected:
        messagebox.showerror("Erro", "Selecione um item para remover.")
        return

    shopping = load_data(shopping_file)

    for item in selected:
        shopping_item = shopping_table.item(item, "values")[0]
        shopping["pending"].remove(shopping_item)

    save_data(shopping_file, shopping)
    update_shopping_table()

def update_shopping_table():
    for row in shopping_table.get_children():
        shopping_table.delete(row)

    shopping = load_data(shopping_file)
    if "pending" in shopping:
        for item in shopping["pending"]:
            shopping_table.insert("", tk.END, values=(item,))

# Configuração da Interface Gráfica
root = tk.Tk()
root.title("Gerenciador de Tarefas e Compras")

# Gerenciador de Tarefas
frame_tasks = tk.LabelFrame(root, text="Tarefas")
frame_tasks.pack(padx=10, pady=10, fill="both", expand=True)

entry_task = tk.Entry(frame_tasks, width=50)
entry_task.pack(pady=5)

btn_add_task = tk.Button(frame_tasks, text="Adicionar Tarefa", command=add_task)
btn_add_task.pack(pady=5)

btn_complete_task = tk.Button(frame_tasks, text="Marcar como Concluída", command=complete_task)
btn_complete_task.pack(pady=5)

btn_history = tk.Button(frame_tasks, text="Histórico", command=show_history)
btn_history.pack(pady=5)

columns = ("Tarefa",)
task_table = ttk.Treeview(frame_tasks, columns=columns, show="headings")
task_table.heading("Tarefa", text="Tarefa")
task_table.pack(pady=5, fill="both", expand=True)

update_task_table()

# Lista de Compras
frame_shopping = tk.LabelFrame(root, text="Lista de Compras")
frame_shopping.pack(padx=10, pady=10, fill="both", expand=True)

entry_item = tk.Entry(frame_shopping, width=50)
entry_item.pack(pady=5)

btn_add_item = tk.Button(frame_shopping, text="Adicionar Item", command=add_shopping_item)
btn_add_item.pack(pady=5)

btn_complete_item = tk.Button(frame_shopping, text="Marcar como Comprado", command=complete_shopping_item)
btn_complete_item.pack(pady=5)

btn_remove_item = tk.Button(frame_shopping, text="Remover Item", command=remove_shopping_item)
btn_remove_item.pack(pady=5)

columns_shopping = ("Item",)
shopping_table = ttk.Treeview(frame_shopping, columns=columns_shopping, show="headings")
shopping_table.heading("Item", text="Item")
shopping_table.pack(pady=5, fill="both", expand=True)

update_shopping_table()

root.mainloop()