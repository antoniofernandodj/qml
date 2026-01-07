import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

import Components 1.0

ApplicationWindow {
    visible: true
    width: 800
    height: 600
    title: "Componentes QML - 2 Formas"
    
    // ===== FORMA 1: COMPONENTE INLINE (definido aqui mesmo) =====
    component SimpleButton: Button {
        id: btn
        property string bgColor: "#28a745"
        
        background: Rectangle {
            radius: 6
            color: btn.pressed ? Qt.darker(btn.bgColor, 1.2) : btn.bgColor
        }
        
        contentItem: Text {
            text: btn.text
            color: "white"
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
        }
    }
    
    ScrollView {
        anchors.fill: parent
        anchors.margins: 20
        
        ColumnLayout {
            width: parent.width - 40
            spacing: 30
            
            Text {
                text: "Componentes QML Reutilizáveis"
                font.pixelSize: 32
                font.weight: Font.Bold
                Layout.alignment: Qt.AlignHCenter
            }

            // ===== USANDO COMPONENTES DE ARQUIVOS SEPARADOS =====
            Card {
                title: "Componentes de Arquivos (./components/)"
                Layout.fillWidth: true
                Layout.preferredHeight: 250
                
                ColumnLayout {
                    anchors.fill: parent
                    spacing: 15
                    
                    Text {
                        text: `Estes componentes estão em arquivos .qml separados`
                        wrapMode: Text.WordWrap
                        Layout.fillWidth: true
                    }
                    
                    Input {
                        label: "Nome"
                        placeholder: "Digite seu nome"
                        Layout.fillWidth: true
                        onTextChanged: {
                            console.log("Nome:", text)
                        }
                    }
                    
                    Input {
                        label: "Email"
                        placeholder: "seu@email.com"
                        Layout.fillWidth: true
                        onTextChanged: {
                            console.log("Nome:", text)
                        }
                    }

                    Row {
                        spacing: 10
                        Layout.alignment: Qt.AlignRight
                        
                        CustomButton {
                            text: "Cancelar"
                            variant: "danger"
                            onClicked: console.log("Cancelado")
                        }
                        
                        CustomButton {
                            text: "Salvar"
                            variant: "primary"
                            onClicked: console.log("Salvo")
                        }
                    }
                }
            }
            
            // ===== USANDO COMPONENTES INLINE =====
            Rectangle {
                Layout.fillWidth: true
                Layout.preferredHeight: 200
                color: "#ffffff"
                radius: 12
                border.width: 1
                border.color: "#e0e0e0"
                
                ColumnLayout {
                    anchors.fill: parent
                    anchors.margins: 20
                    spacing: 15
                    
                    Text {
                        text: "Componentes Inline (definidos no mesmo arquivo)"
                        font.pixelSize: 20
                        font.weight: Font.Bold
                    }
                    
                    Text {
                        text: "Estes componentes são definidos com 'component' no QML"
                        wrapMode: Text.WordWrap
                        Layout.fillWidth: true
                    }
                    
                    Row {
                        spacing: 10
                        
                        SimpleButton {
                            text: "Success"
                            bgColor: "#28a745"
                            onClicked: console.log("Success!")
                        }
                        
                        SimpleButton {
                            text: "Warning"
                            bgColor: "#ffc107"
                            onClicked: console.log("Warning!")
                        }
                        
                        SimpleButton {
                            text: "Info"
                            bgColor: "#17a2b8"
                            onClicked: console.log("Info!")
                        }
                    }
                    
                    SimpleButton {
                        text: counterVM ? "Contador: " + counterVM.counter : "Contador: 0"
                        bgColor: "#6f42c1"
                        Layout.preferredWidth: 200
                        onClicked: if (counterVM) counterVM.increment()
                    }
                }
            }
            
            // ===== COMPARAÇÃO =====
            Rectangle {
                Layout.fillWidth: true
                Layout.preferredHeight: 200
                color: "#f8f9fa"
                radius: 12
                
                ColumnLayout {
                    anchors.fill: parent
                    anchors.margins: 20
                    spacing: 10
                    
                    Text {
                        text: "📚 Quando usar cada abordagem?"
                        font.pixelSize: 18
                        font.weight: Font.Bold
                    }
                    
                    Text {
                        text: "✅ Arquivos separados: Para componentes reutilizáveis em múltiplas telas"
                        wrapMode: Text.WordWrap
                        Layout.fillWidth: true
                    }
                    
                    Text {
                        text: "✅ Inline (component): Para componentes específicos de uma tela"
                        wrapMode: Text.WordWrap
                        Layout.fillWidth: true
                    }
                    
                    Text {
                        text: "💡 Dica: Comece inline e mova para arquivo quando precisar reutilizar"
                        wrapMode: Text.WordWrap
                        Layout.fillWidth: true
                        color: "#0066cc"
                    }
                }
            }
        }
    }
}