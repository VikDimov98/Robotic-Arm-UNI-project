import tkinter as tk
import api as wrapper


def main():
    """
    Main function. Creates the window to display. Can be called whenever you want the configuration dialog to appear.
    :return: None
    """
    # Window instance
    window = tk.Tk()

    def save_config():
        """
        Callback function for whenever save button is pressed
        :return: None
        """
        wrapper.set_ip(ip_input.get())
        wrapper.set_port(port_input.get())
        # wrapper.set_url(url_input.get())
        wrapper.set_use_save_connection(bool(use_https.get()))
        wrapper._write_config()
        window.destroy()

    # Headline
    headline = tk.Label(text="Robotic hand api configuration")
    headline.grid(row=0, column=0, columnspan=2)

    # Ip input
    ip_label = tk.Label(text="IP:", anchor='e')
    ip_label.grid(row=1, column=0)
    ip_input = tk.Entry()
    ip_input.insert(0, wrapper._config['ip'])
    ip_input.grid(row=1, column=1)

    # Port input
    port_label = tk.Label(text="Port:", anchor='e')
    port_label.grid(row=2, column=0)
    port_input = tk.Entry()
    port_input.insert(0, wrapper._config['port'])
    port_input.grid(row=2, column=1)

    # Save connection
    use_https = tk.IntVar()
    if wrapper._config['save']:
        use_https = tk.IntVar(value=1)
    https_checkbox = tk.Checkbutton(text="Use HTTPS", variable=use_https)
    https_checkbox.grid(row=3, column=0, columnspan=2)

    # Save button
    save_button = tk.Button(text="Save", width=20, height=3, command=save_config)
    save_button.grid(row=4, column=0, columnspan=2)

    # Launches window
    window.mainloop()


if __name__ == '__main__':
    # Calls main function. This allows it to work as standalone as well as a part of something bigger
    main()
