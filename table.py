from tkinter import Frame, W, Message, CENTER, Label, X, N, E, S, StringVar, END, Entry
from tkinter.ttk import Combobox
from typing import Dict, List


class Cell(Frame):
    """Base class for cells"""


class DataEntryCell(Cell):
    def __init__(
        self,
        master,
        variable,
        disabled: bool = False,
        anchor=W,
        bordercolor=None,
        borderwidth=1,
        padx=0,
        pady=0,
        background=None,
        foreground=None,
        font=None,
    ):
        Cell.__init__(
            self,
            master,
            background=background,
            highlightbackground=bordercolor,
            highlightcolor=bordercolor,
            highlightthickness=borderwidth,
            bd=0,
        )

        self._message_widget = Entry(
            self,
            bd=0,
            textvariable=variable,
            font=font,
            background=background,
            foreground=foreground,
            state="disabled" if disabled else "normal",
        )
        self._message_widget.pack(expand=True, padx=padx, pady=pady, anchor=anchor)


class DataComboboxCell(Cell):
    def __init__(
        self,
        master,
        variable,
        values=None,
        anchor=W,
        bordercolor=None,
        borderwidth=1,
        padx=0,
        pady=0,
        background=None,
        foreground=None,
        font=None,
    ):
        Cell.__init__(
            self,
            master,
            background=background,
            highlightbackground=bordercolor,
            highlightcolor=bordercolor,
            highlightthickness=borderwidth,
            bd=0,
        )

        values = values or []
        self._message_widget = Combobox(
            self,
            textvariable=variable,
            values=values,
            font=font,
            background=background,
            foreground=foreground,
        )
        self._message_widget.pack(expand=True, padx=padx, pady=pady, anchor=anchor)


class HeaderCell(Cell):
    def __init__(
        self,
        master,
        text,
        bordercolor=None,
        borderwidth=1,
        padx=None,
        pady=None,
        background=None,
        foreground=None,
        font=None,
        anchor=CENTER,
    ):
        Cell.__init__(
            self,
            master,
            background=background,
            highlightbackground=bordercolor,
            highlightcolor=bordercolor,
            highlightthickness=borderwidth,
            bd=0,
        )
        self._header_label = Label(
            self, text=text, background=background, foreground=foreground, font=font
        )
        self._header_label.pack(padx=padx, pady=pady, expand=True)

        if bordercolor is not None:
            separator = Frame(
                self,
                height=2,
                background=bordercolor,
                bd=0,
                highlightthickness=0,
                class_="Separator",
            )
            separator.pack(fill=X, anchor=anchor)


class Table(Frame):
    def __init__(
        self,
        master,
        columns,
        disabled_inp_column: List = None,
        comboboxes: Dict = None,
        column_weights=None,
        column_minwidths=None,
        height=None,
        padx=3,
        pady=3,
        cell_font=None,
        cell_foreground="black",
        cell_background="white",
        cell_anchor=W,
        header_font=None,
        header_background="white",
        header_foreground="black",
        header_anchor=CENTER,
        bordercolor="#999999",
        innerborder=True,
        outerborder=True,
        stripped_rows=("#EEEEEE", "white"),
        on_change_data=None,
    ):

        outerborder_width = 1 if outerborder else 0

        Frame.__init__(
            self,
            master,
            highlightbackground=bordercolor,
            highlightcolor=bordercolor,
            highlightthickness=outerborder_width,
            bd=0,
        )

        self._cell_background = cell_background
        self._cell_foreground = cell_foreground
        self._cell_font = cell_font
        self._cell_anchor = cell_anchor

        self._number_of_rows = 0
        self._number_of_columns = len(columns)
        self._comboboxes = comboboxes or {}
        self._disabled_inputs = disabled_inp_column or []

        self._stripped_rows = stripped_rows

        self._padx = padx
        self._pady = pady

        self._bordercolor = bordercolor
        self._innerborder_width = 1 if innerborder else 0

        self._data_vars = []

        self._columns = columns

        for j in range(len(columns)):
            column_name = columns[j]

            header_cell = HeaderCell(
                self,
                text=column_name,
                borderwidth=self._innerborder_width,
                font=header_font,
                background=header_background,
                foreground=header_foreground,
                padx=padx,
                pady=pady,
                bordercolor=bordercolor,
                anchor=header_anchor,
            )
            header_cell.grid(row=0, column=j, sticky=N + E + W + S)

        if column_weights is None:
            for j in range(len(columns)):
                self.grid_columnconfigure(j, weight=1)
        else:
            for j, weight in enumerate(column_weights):
                self.grid_columnconfigure(j, weight=weight)

        if column_minwidths is None:
            column_minwidths = [None for _ in columns]
        self.update_idletasks()
        for j, minwidth in enumerate(column_minwidths):
            if minwidth is None:
                header_cell = self.grid_slaves(row=0, column=j)[0]
                minwidth = header_cell.winfo_reqwidth()
            self.grid_columnconfigure(j, minsize=minwidth)

        if height is not None:
            self.append_n_rows(height)

        self._on_change_data = on_change_data

    def append_n_rows(self, n):
        number_of_rows = self._number_of_rows
        number_of_columns = self._number_of_columns
        cnf = dict(
            borderwidth=self._innerborder_width,
            bordercolor=self._bordercolor,
            padx=self._padx,
            pady=self._pady,
            foreground=self._cell_foreground,
            font=self._cell_font,
            anchor=self._cell_anchor,
        )

        for i in range(number_of_rows + 1, number_of_rows + n + 1):
            list_of_vars = []
            for j in range(number_of_columns):
                var = StringVar()
                list_of_vars.append(var)
                bg = self._stripped_rows[(i + 1) % 2]
                cnf["background"] = bg
                if str(j) not in self._comboboxes.keys():
                    cell = DataEntryCell(
                        self, disabled=j in self._disabled_inputs, variable=var, **cnf
                    )
                else:
                    cell = DataComboboxCell(
                        self, variable=var, values=self._comboboxes[str(j)], **cnf
                    )
                cell.grid(row=i, column=j, sticky=N + E + W + S)

            self._data_vars.append(list_of_vars)

        self._number_of_rows += n

    def pop_n_rows(self, n: int = 1):
        number_of_rows = self._number_of_rows
        number_of_columns = self._number_of_columns
        for i in range(number_of_rows - n + 1, number_of_rows + 1):
            for j in range(number_of_columns):
                self.grid_slaves(row=i, column=j)[0].destroy()

            self._data_vars.pop()

        self._number_of_rows -= n

    def set_data(self, data):
        n = len(data)
        m = len(data[0])

        number_of_rows = self._number_of_rows

        if number_of_rows > n:
            self.pop_n_rows(number_of_rows - n)
        elif number_of_rows < n:
            self.append_n_rows(n - number_of_rows)

        for i in range(n):
            for j in range(m):
                self._data_vars[i][j].set(data[i][j])

        if self._on_change_data is not None:
            self._on_change_data()

    def get_data(self):
        number_of_rows = self._number_of_rows
        number_of_columns = self._number_of_columns

        data = []
        for i in range(number_of_rows):
            row = []
            row_of_vars = self._data_vars[i]
            for j in range(number_of_columns):
                cell_data = row_of_vars[j].get()
                row.append(cell_data)

            data.append(row)
        return data

    @property
    def number_of_rows(self):
        return self._number_of_rows

    @property
    def number_of_columns(self):
        return self._number_of_columns

    def row(self, index, data=None):
        number_of_columns = self._number_of_columns

        if data is None:
            row = []
            row_of_vars = self._data_vars[index]

            for j in range(number_of_columns):
                row.append(row_of_vars[j].get())

            return row
        else:
            if len(data) != number_of_columns:
                raise ValueError(
                    "data has no %d elements: %s" % (number_of_columns, data)
                )

            row_of_vars = self._data_vars[index]
            for j in range(number_of_columns):
                row_of_vars[index][j].set(data[j])

            if self._on_change_data is not None:
                self._on_change_data()

    def column(self, index, data=None):
        number_of_rows = self._number_of_rows

        if data is None:
            column = []

            for i in range(number_of_rows):
                column.append(self._data_vars[i][index].get())

            return column
        else:

            if len(data) != number_of_rows:
                raise ValueError("data has no %d elements: %s" % (number_of_rows, data))

            for i in range(self._number_of_columns):
                self._data_vars[i][index].set(data[i])

            if self._on_change_data is not None:
                self._on_change_data()

    def clear(self):
        number_of_rows = self._number_of_rows
        number_of_columns = self._number_of_columns

        for i in range(number_of_rows):
            for j in range(number_of_columns):
                self._data_vars[i][j].set("")

        if self._on_change_data is not None:
            self._on_change_data()

    def delete_row(self, index: int):
        i = index
        while i < self._number_of_rows - 1:
            row_of_vars_1 = self._data_vars[i]
            row_of_vars_2 = self._data_vars[i + 1]

            j = 0
            while j < self._number_of_columns:
                row_of_vars_1[j].set(row_of_vars_2[j].get())
                j += 1

            i += 1

        self.pop_n_rows(1)

        if self._on_change_data is not None:
            self._on_change_data()

    def insert_row(self, data, index=END):
        self.append_n_rows(1)

        if index == END:
            index = self._number_of_rows - 1

        i = self._number_of_rows - 1
        while i > index:
            row_of_vars_1 = self._data_vars[i - 1]
            row_of_vars_2 = self._data_vars[i]

            j = 0
            while j < self._number_of_columns:
                row_of_vars_2[j].set(row_of_vars_1[j])
                j += 1
            i -= 1

        list_of_cell_vars = self._data_vars[index]
        for cell_var, cell_data in zip(list_of_cell_vars, data):
            cell_var.set(cell_data)

        if self._on_change_data is not None:
            self._on_change_data()

    def cell(self, row, column, data=None):
        """Get the value of a table cell"""
        if data is None:
            return self._data_vars[row][column].get()
        else:
            self._data_vars[row][column].set(data)
            if self._on_change_data is not None:
                self._on_change_data()

    def __getitem__(self, index):
        if isinstance(index, tuple):
            row, column = index
            return self.cell(row, column)
        else:
            raise Exception("Row and column indices are required")

    def __setitem__(self, index, value):
        if isinstance(index, tuple):
            row, column = index
            self.cell(row, column, value)
        else:
            raise Exception("Row and column indices are required")

    def on_change_data(self, callback):
        self._on_change_data = callback
