from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """
    Специальный класс, который отвечает за
    обработку входящих запросов от клиентов
    """

    def do_GET(self):
        """Метод для обработки входящих GET-запросов"""

        if self.path == "/":
            try:
                with open("contacts.html", encoding="utf-8") as f:
                    content = f.read()
                    self.send_response(200)  # Отправка кода ответа
                    self.send_header("Content-type", "text/html")
                    # Отправка типа данных, который будет передаваться
                    self.end_headers()  # Завершение формирования заголовков ответа
                    self.wfile.write(bytes(content, "utf-8"))  # Тело ответа
            except FileNotFoundError:
                self.send_response(404)
        elif self.path.startswith("/css/"):
            try:
                with open("css/bootstrap.min.css", encoding="utf-8") as f:
                    css_style = f.read()
                    self.send_response(200)  # Отправка кода ответа
                    self.send_header("Content-type", "text/css")
                    # Отправка типа данных, который будет передаваться
                    self.end_headers()  # Завершение формирования заголовков ответа
                    self.wfile.write(bytes(css_style, "utf-8"))  # Тело ответа
            except FileNotFoundError:
                self.send_response(404)
        else:
            self.send_response(404)


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через
        # сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес
    # и порт в сети, которые занимал
    webServer.server_close()
    print("Server stopped.")
