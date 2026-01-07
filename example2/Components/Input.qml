import QtQuick
import QtQuick.Controls

Column {
    id: root
    
    // Props
    property string label: ""
    property string placeholder: ""
    property alias text: textField.text
    
    spacing: 8

    Text {
        visible: root.label !== ""
        text: root.label
        font.pixelSize: 14
        font.weight: Font.Medium
        color: "#2c3e50"
    }
    
    // Input field
    TextField {
        id: textField
        width: parent.width
        placeholderText: root.placeholder
        
        background: Rectangle {
            radius: 6
            color: "#ffffff"
            border.width: textField.activeFocus ? 2 : 1
            border.color: textField.activeFocus ? "#007bff" : "#ced4da"
            
            Behavior on border.color {
                ColorAnimation { duration: 150 }
            }
        }
    }
}
