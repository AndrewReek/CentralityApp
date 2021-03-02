import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
import GraphGenerator as gg
import Centrality as C


WINDOW_SIZE = '900x600'
BG_COLOR = '#234183'

file_path = ''

class main_window(tk.Frame):
    def __init__(self, master = None):
        tk.Canvas.__init__(self, master)

        self.master = master
        self.init_window()


    def init_window(self):
        self.master.title('Network Generator Tool')

        M = tk.Menu(self.master)
        self.master.config(menu=M)

        ###### Frames, buttons, labels, and checkboxes ######
        input_file_frame = tk.Frame(self.master, bg='white')
        input_file_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.05, anchor='n')
        input_file_button = ttk.Button(input_file_frame, text='Import File', command=lambda: get_file(input_file_frame))
        input_file_button.place(relx=0.99, rely=0.5, relwidth=0.1, relheight=0.9, anchor='e')

        ###Column names stuff (left side)
        column_names_frame = tk.Frame(self.master, bg='white')
        column_names_frame.place(relx=0.3, rely=0.25, relwidth=0.33, relheight=0.5, anchor='n')
        col_names_label = tk.Label(column_names_frame, text='Import Data Column Names', background='white', font=35)
        col_names_label.place(relx=0.5, rely=0.05, anchor='n')

        inv_name_label = tk.Label(column_names_frame, text='Investor Name:', background='white')
        inv_name_label.place(relx=0.1, rely=0.22, anchor='nw')
        inv_name_entry = ttk.Entry(column_names_frame)
        inv_name_entry.place(relx=0.08, rely=0.30, relwidth=0.84, anchor='nw')

        company_id_label = tk.Label(column_names_frame, text='Company ID:', background='white')
        company_id_label.place(relx=0.1, rely=0.38, anchor='nw')
        company_id_entry = ttk.Entry(column_names_frame)
        company_id_entry.place(relx=0.08, rely=0.46, relwidth=0.84, anchor='nw')

        inv_amt_label = tk.Label(column_names_frame, text='Investment Amount:', background='white')
        inv_amt_label.place(relx=0.1, rely=0.54, anchor='nw')
        inv_amt_entry = ttk.Entry(column_names_frame)
        inv_amt_entry.place(relx=0.08, rely=0.62, relwidth=0.84, anchor='nw')

        ###Centrality measures stuff (right side)
        centrality_check_frame = tk.Frame(self.master, bg='white')
        centrality_check_frame.place(relx=0.7, rely=0.25, relwidth=0.33, relheight=0.5, anchor='n')
        centrality_name_label = tk.Label(centrality_check_frame, text='Centrality Measures', background='white', font=35)
        centrality_name_label.place(relx=0.5, rely=0.05, anchor='n')

        degree_cent_label = tk.Label(centrality_check_frame, text='Degree Centrality:', background='white')
        degree_cent_label.place(relx=0.1, rely=0.22, anchor='nw')
        degree_run = tk.BooleanVar()
        degree_cent_check = tk.Checkbutton(centrality_check_frame, bg='white', variable=degree_run, offvalue=False, onvalue=True)
        degree_cent_check.place(relx=0.8, rely=0.22, anchor='nw')

        eigen_label = tk.Label(centrality_check_frame, text='Eigenvector Centrality:', background='white')
        eigen_label.place(relx=0.1, rely=0.30, anchor='nw')
        eigen_run = tk.BooleanVar()
        eigen_check = tk.Checkbutton(centrality_check_frame, bg='white', variable=eigen_run, offvalue=False, onvalue=True)
        eigen_check.place(relx=0.8, rely=0.30, anchor='nw')

        between_label = tk.Label(centrality_check_frame, text='Betweenness Centrality:', background='white')
        between_label.place(relx=0.1, rely=0.38, anchor='nw')
        between_run = tk.BooleanVar()
        between_check = tk.Checkbutton(centrality_check_frame, bg='white', variable=between_run, offvalue=False, onvalue=True)
        between_check.place(relx=0.8, rely=0.38, anchor='nw')

        close_label = tk.Label(centrality_check_frame, text='Closeness Centrality:', background='white')
        close_label.place(relx=0.1, rely=0.46, anchor='nw')
        close_run = tk.BooleanVar()
        close_check = tk.Checkbutton(centrality_check_frame, bg='white', variable=close_run, offvalue=False, onvalue=True)
        close_check.place(relx=0.8, rely=0.46, anchor='nw')

        load_label = tk.Label(centrality_check_frame, text='Load Centrality:', background='white')
        load_label.place(relx=0.1, rely=0.54, anchor='nw')
        load_run = tk.BooleanVar()
        load_check = tk.Checkbutton(centrality_check_frame, bg='white', variable=load_run, offvalue=False, onvalue=True)
        load_check.place(relx=0.8, rely=0.54, anchor='nw')

        subgraph_label = tk.Label(centrality_check_frame, text='Subgraph Centrality:', background='white')
        subgraph_label.place(relx=0.1, rely=0.62, anchor='nw')
        subgraph_run = tk.BooleanVar()
        subgraph_check = tk.Checkbutton(centrality_check_frame, bg='white', variable=subgraph_run, offvalue=False, onvalue=True)
        subgraph_check.place(relx=0.8, rely=0.62, anchor='nw')

        harmonic_label = tk.Label(centrality_check_frame, text='Harmonic Centrality:', background='white')
        harmonic_label.place(relx=0.1, rely=0.7, anchor='nw')
        harmonic_run = tk.BooleanVar()
        harmonic_check = tk.Checkbutton(centrality_check_frame, bg='white', variable=harmonic_run, offvalue=False, onvalue=True)
        harmonic_check.place(relx=0.8, rely=0.7, anchor='nw')

        ###Run button
        run_button = ttk.Button(self.master, text='Run',
                                command=lambda: run(file_path, inv_name_entry, company_id_entry,
                                                    inv_amt_entry, degree_run, eigen_run, between_run,
                                                    close_run, load_run, subgraph_run, harmonic_run))
        run_button.place(relx=0.75, rely=0.80)

        ###### Menu bar stuff ######
        file = tk.Menu(M)
        file.add_command(label='Import', command=lambda: get_file(input_file_frame))
        file.add_command(label='Exit', command=self.client_exit)
        M.add_cascade(label='File', menu=file)

        help = tk.Menu(M)
        help.add_command(label='About', command=self.show_about)
        M.add_cascade(label='Help', menu=help)

    def client_exit(self):
        exit()

    def show_about(self):
        pass


def get_file(parent):
    global file_path 
    input_file_label = ttk.Label(parent, background='white', text='')
    filename = filedialog.askopenfilename(title='File Import', filetypes=(('CSV Files', '*.csv'),))
    file_path = str(filename)
    input_file_label = ttk.Label(parent, background='white', text=file_path)
    input_file_label.place(relx=0.01, rely=0, relheight=1)

def run(file_path, inv_name, firm_id, inv_amt, degree_run, eigen_run, between_run, close_run,
        load_run, subgraph_run, harmonic_run):
    inv_name = inv_name.get()
    firm_id = firm_id.get()
    inv_amt = inv_amt.get()

    df = gg.read_file(file_path, inv_name, firm_id, inv_amt)
    edgelist = gg.generate_edgelist(df)
    graph = gg.generate_graph(edgelist)
    adj_mat = gg.generate_matrix(graph)

    cent_df_list = []
    degree_df = C.get_degree(graph, degree_run.get())
    eigen_df = C.get_eigenvector(graph, eigen_run.get())
    between_df = C.get_betweenness(graph, between_run.get())
    close_df = C.get_closeness(graph, close_run.get())
    load_df = C.get_load(graph, load_run.get())
    subgraph_df = C.get_subgraph(graph, subgraph_run.get())
    harmonic_df = C.get_harmonic(graph, harmonic_run.get())
    cent_df_list.append(degree_df)
    cent_df_list.append(eigen_df)
    cent_df_list.append(between_df)
    cent_df_list.append(close_df)
    cent_df_list.append(load_df)
    cent_df_list.append(subgraph_df)
    cent_df_list.append(harmonic_df)

    cent_df = pd.concat(cent_df_list)
    cent_df = cent_df.transpose()
    gg.export_graph(cent_df, 'centralitymeasures.csv')
    gg.export_graph(edgelist, 'edgelist.csv')
    gg.export_graph(adj_mat, 'adjacencymatrix.csv')
    

root = tk.Tk()
root.geometry(WINDOW_SIZE)
root.configure(bg = BG_COLOR)
root.iconbitmap('programicon_Aj7_icon.ico')
centrality_app = main_window(root)
root.mainloop()