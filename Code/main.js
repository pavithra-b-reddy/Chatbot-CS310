const path = require('path');
const os = require('os');

const { app, BrowserWindow, Menu, ipcMain, shell } = require('electron');

// Set Environment
process.env.NODE_ENV = 'development';
const isDev = process.env.NODE_ENV !== 'production' ? true : false;
const isMac = process.platform === 'darwin' ? true : false

let MainWindow;

function createMainWindow() {
    MainWindow = new BrowserWindow({
        title: 'Chatbot',
        width: 600,
        height: 600,
        resizable: isDev,
        backgroundColor: 'white',
        webPreferences: {
            nodeIntegration: true,
            enableRemoteModule: true
        }

    });

    MainWindow.loadFile('./start.html');
}

app.on('ready', () => {
  createMainWindow();

  MainWindow.on('ready', () => MainWindow = null);
});

app.on('window-all-closed', () => {
    if (!isMac) {
      app.quit()
    }
  })

  app.on('activate', () => {
    // On macOS it's common to re-create a window in the app when the
    // dock icon is clicked and there are no other windows open.
    if (BrowserWindow.getAllWindows().length === 0) {
      createMainWindow()
    }
  })
