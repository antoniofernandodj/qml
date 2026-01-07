import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


ApplicationWindow {
  visible: true
  width: 600
  height: 700
  title: "Padrão Reativo - PySide6 + QML"

  ColumnLayout {
    anchors.fill: parent
    anchors.margins: 20
    spacing: 20
    
    // Seção do Counter (ViewModel reativo)
    Rectangle {
      Layout.fillWidth: true
      Layout.preferredHeight: 250
      color: "#f0f0f0"
      radius: 10
      
      ColumnLayout {
        anchors.fill: parent
        anchors.margins: 20
        spacing: 15
        
        Text {
          text: "Counter Reativo"
          font.pixelSize: 24
          font.bold: true
          Layout.alignment: Qt.AlignHCenter
        }
        
        Text {
          // Binding reativo - atualiza automaticamente quando counter muda
          text: counterVM ? counterVM.counter : 0
          font.pixelSize: 48
          font.bold: true
          color: (counterVM && counterVM.counter > 5) ? "#e74c3c" : "#3498db"
          Layout.alignment: Qt.AlignHCenter
        }
        
        Text {
          // Binding reativo - atualiza quando message muda
          text: counterVM ? counterVM.message : ""
          font.pixelSize: 18
          color: "#7f8c8d"
          Layout.alignment: Qt.AlignHCenter
        }
        
        RowLayout {
          Layout.alignment: Qt.AlignHCenter
          spacing: 10
          
          Button {
            text: "➖"
            font.pixelSize: 20
            enabled: counterVM !== null
            onClicked: {
              if (counterVM) counterVM.decrement()
            }
          }
          
          Button {
            text: "Reset"
            enabled: counterVM !== null
            onClicked: {
              if (counterVM) counterVM.reset()
            }
          }
          
          Button {
            text: "➕"
            font.pixelSize: 20
            enabled: counterVM !== null
            onClicked: {
              if (counterVM) counterVM.increment()
            }
          }
        }
      }
    }
    
    // Seção da Lista de Tarefas (Model reativo)
    Rectangle {
      Layout.fillWidth: true
      Layout.fillHeight: true
      color: "#f0f0f0"
      radius: 10
      
      ColumnLayout {
        anchors.fill: parent
        anchors.margins: 20
        spacing: 15
        
        Text {
          text: "Lista de Tarefas Reativa"
          font.pixelSize: 24
          font.bold: true
        }
        
        RowLayout {
          Layout.fillWidth: true
          spacing: 10
          
          TextField {
            id: taskInput
            Layout.fillWidth: true
            placeholderText: "Nova tarefa..."
            enabled: taskListModel !== null
            onAccepted: {
              if (taskListModel && text.trim()) {
                taskListModel.addTask(text)
                text = ""
              }
            }
          }
            
          Button {
            text: "Adicionar"
            enabled: taskListModel !== null
            onClicked: {
              if (taskListModel && taskInput.text.trim()) {
                taskListModel.addTask(taskInput.text)
                taskInput.text = ""
              }
            }
          }
        }
        
        ListView {
          Layout.fillWidth: true
          Layout.fillHeight: true
          clip: true
          spacing: 5
          
          // Binding reativo ao model
          model: taskListModel ? taskListModel : null
          
          delegate: Rectangle {
            width: ListView.view.width
            height: 50
            color: model.completed ? "#d5f4e6" : "white"
            radius: 5
            border.color: "#bdc3c7"
            border.width: 1
            
            RowLayout {
              anchors.fill: parent
              anchors.margins: 10
              spacing: 10
              
              CheckBox {
                checked: model.completed
                onClicked: {
                  if (taskListModel) taskListModel.toggleTask(index)
                }
              }

              Text {
                text: model.text
                font.pixelSize: 16
                font.strikeout: model.completed
                color: model.completed ? "#7f8c8d" : "black"
                Layout.fillWidth: true
              }

              Button {
                text: "✖"
                flat: true
                onClicked: {
                  if (taskListModel) taskListModel.removeTask(index)
                }
              }
            }
          }
        }
      }
    }
  }
}