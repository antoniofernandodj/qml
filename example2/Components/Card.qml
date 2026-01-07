import QtQuick
import QtQuick.Layouts

Rectangle {
    id: root

    // Props
    property string title: ""
    default property alias content: contentItem.data  // Permite children

    color: "#ffffff"
    radius: 12
    border.width: 1
    border.color: "#e0e0e0"

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 20
        spacing: 15

        // Header
        Text {
            visible: root.title !== ""
            text: root.title
            font.pixelSize: 20
            font.weight: Font.Bold
            color: "#2c3e50"
            Layout.fillWidth: true
        }
        
        // Separator
        Rectangle {
            visible: root.title !== ""
            Layout.fillWidth: true
            height: 1
            color: "#e0e0e0"
        }
        
        // Content (children vão aqui)
        Item {
            id: contentItem
            Layout.fillWidth: true
            Layout.fillHeight: true
        }
    }
}
