import QtQuick
import QtQuick.Controls

Button {
    id: root
    
    // Props (propriedades públicas)
    property string variant: "primary"  // primary, secondary, danger
    
    implicitWidth: 120
    implicitHeight: 40
    
    background: Rectangle {
        radius: 8
        color: {
            if (!root.enabled) return "#cccccc"
            if (root.pressed) {
                return root.variant === "danger" ? "#bd2130" : "#004085"
            }
            if (root.hovered) {
                return root.variant === "danger" ? "#c82333" : "#0056b3"
            }
            return root.variant === "danger" ? "#dc3545" : "#007bff"
        }
        
        Behavior on color {
            ColorAnimation { duration: 150 }
        }
    }
    
    contentItem: Text {
        text: root.text
        color: "white"
        font.weight: Font.Medium
        font.pixelSize: 14
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
    }
}
