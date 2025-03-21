import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox, QInputDialog

# Datos de ejemplo
participante1 = {
    'nombre': 'Dara',
    'grado': '2do', 
    'tipo de Evento': 'Social',
    'tipo de participación': 'Decoracion'
}
participante2 = {
    'nombre': 'Edgar',
    'grado': '2do', 
    'tipo de Evento': 'Escolar',
    'tipo de participación': 'Decoracion'
}
participante3 = {
    'nombre': 'Irving',
    'grado': '2do', 
    'tipo de Evento': 'Escolar',
    'tipo de participación': 'Decoracion'
}


participantes_list = [participante1, participante2, participante3]

class MainWindow(QMainWindow):
    def __init__(self):  
        super().__init__()  
        print("Inicializando MainWindow...")
        self.setWindowTitle("Organizador de Eventos Escolares")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.btn_agregar = QPushButton("Registrar Participante")
        self.btn_agregar.clicked.connect(self.agregar_participante)
        layout.addWidget(self.btn_agregar)

        self.btn_eliminar = QPushButton("Eliminar Participante")
        self.btn_eliminar.clicked.connect(self.eliminar_participante)
        layout.addWidget(self.btn_eliminar)

        self.btn_modificar = QPushButton("Modificar Participante")
        self.btn_modificar.clicked.connect(self.modificar_participante)
        layout.addWidget(self.btn_modificar)

        self.btn_consultar = QPushButton("Consultar Participantes")
        self.btn_consultar.clicked.connect(self.consultar_participantes)
        layout.addWidget(self.btn_consultar)

        self.btn_salir = QPushButton("Salir")
        self.btn_salir.clicked.connect(self.close)
        layout.addWidget(self.btn_salir)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        print("Ventana configurada correctamente.")

    def agregar_participante(self):
        print("Agregando participante...")
        nombre, ok = QInputDialog.getText(self, 'Registrar Participante', 'Ingresa el nombre del participante:')
        if ok:
            grado, ok = QInputDialog.getText(self, 'Registrar Participante', 'Ingresa el grado:')
            if ok:
                evento, ok = QInputDialog.getText(self, 'Registrar Participante', 'Ingresa el tipo de evento:')
                if ok:
                    participacion, ok = QInputDialog.getText(self, 'Registrar Participante', 'Ingresa el tipo de participación:')
                    if ok:
                        nuevo_participante = {
                            "nombre": nombre,
                            "grado": grado,
                            "tipo de Evento": evento,
                            "tipo de participación": participacion
                        }
                        participantes_list.append(nuevo_participante)
                        QMessageBox.information(self, "Éxito", "Participante agregado correctamente.")

    def eliminar_participante(self):
        print("Eliminando participante...")
        if not participantes_list:
            QMessageBox.warning(self, "Error", "No hay participantes en la lista.")
            return

        nombres = [participante['nombre'] for participante in participantes_list]
        nombre, ok = QInputDialog.getItem(self, 'Eliminar Participante', 'Selecciona el nombre del participante a eliminar:', nombres, 0, False)
        if ok:
            for participante in participantes_list:
                if participante['nombre'] == nombre:
                    participantes_list.remove(participante)
                    QMessageBox.information(self, "Éxito", f"El participante {nombre} ha sido eliminado.")
                    return

    def modificar_participante(self):
        print("Modificando participante...")
        if not participantes_list:
            QMessageBox.warning(self, "Error", "No hay participantes en la lista.")
            return

        nombres = [participante['nombre'] for participante in participantes_list]
        nombre, ok = QInputDialog.getItem(self, 'Modificar Participante', 'Selecciona el nombre del participante a modificar:', nombres, 0, False)
        if ok:
            for participante in participantes_list:
                if participante['nombre'] == nombre:
                    opciones = ["Nombre", "Grado", "Tipo de Evento", "Tipo de participación"]
                    opcion, ok = QInputDialog.getItem(self, 'Modificar Participante', '¿Qué deseas modificar?', opciones, 0, False)
                    if ok:
                        if opcion == "Nombre":
                            nuevo_nombre, ok = QInputDialog.getText(self, 'Modificar Participante', 'Ingresa el nuevo nombre:')
                            if ok:
                                participante['nombre'] = nuevo_nombre
                                QMessageBox.information(self, "Éxito", f"El nombre se ha modificado a {nuevo_nombre}")
                        elif opcion == "Grado":
                            nuevo_grado, ok = QInputDialog.getText(self, 'Modificar Participante', 'Ingresa el nuevo grado:')
                            if ok:
                                participante['grado'] = nuevo_grado
                                QMessageBox.information(self, "Éxito", f"El grado se ha modificado a {nuevo_grado}")
                        elif opcion == "Tipo de Evento":
                            nuevo_evento, ok = QInputDialog.getText(self, 'Modificar Participante', 'Ingresa el nuevo tipo de evento:')
                            if ok:
                                participante['tipo de Evento'] = nuevo_evento
                                QMessageBox.information(self, "Éxito", f"El tipo de evento se ha modificado a {nuevo_evento}")
                        elif opcion == "Tipo de participación":
                            nuevo_participacion, ok = QInputDialog.getText(self, 'Modificar Participante', 'Ingresa el nuevo tipo de participación:')
                            if ok:
                                participante['tipo de participación'] = nuevo_participacion
                                QMessageBox.information(self, "Éxito", f"El tipo de participación se ha modificado a {nuevo_participacion}")

    def consultar_participantes(self):
        print("Consultando participantes...")
        if not participantes_list:
            QMessageBox.warning(self, "Error", "No hay participantes disponibles.")
            return

        opciones = ["Ordenados por nombre", "Ordenados por tipo de evento"]
        opcion, ok = QInputDialog.getItem(self, 'Consultar Participantes', '¿Cómo te gustaría visualizar los participantes?', opciones, 0, False)
        if ok:
            if opcion == "Ordenados por nombre":
                participantes_ordenados = sorted(participantes_list, key=lambda x: x['nombre'].lower())
                self.mostrar_participantes(participantes_ordenados, "Participantes ordenados por Nombre:")
            elif opcion == "Ordenados por tipo de evento":
                participantes_ordenados = sorted(participantes_list, key=lambda x: x['tipo de Evento'])
                self.mostrar_participantes(participantes_ordenados, "Participantes ordenados por tipo de evento:")

    def mostrar_participantes(self, participantes, titulo):
        print("Mostrando participantes...")
        dialog = QMessageBox(self)
        dialog.setWindowTitle(titulo)
        dialog.setText("\n".join([f"Nombre: {p['nombre']}, Grado: {p['grado']}, Tipo de Evento: {p['tipo de Evento']}, Tipo de participación: {p['tipo de participación']}" for p in participantes]))
        dialog.exec()

if __name__ == "__main__":
    print("Iniciando aplicación...")
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())