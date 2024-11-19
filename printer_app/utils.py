import win32print
import win32ui
import win32api
import win32con

def print_message(printer_name, message):
    try:
        # Get the printer handle
        printer_handle = win32print.OpenPrinter(printer_name)
    except Exception as e:
        return False, f"OpenPrinter failed: {e}"

    try:
        # Create a device context for the printer
        printer_dc = win32ui.CreateDC()
        printer_dc.CreatePrinterDC(printer_name)
    except Exception as e:
        win32print.ClosePrinter(printer_handle)
        return False, f"CreatePrinterDC failed: {e}"

    try:
        printer_dc.StartDoc('Test Document')
    except Exception as e:
        printer_dc.DeleteDC()
        win32print.ClosePrinter(printer_handle)
        return False, f"StartDoc failed: {e}"

    try:
        printer_dc.StartPage()
    except Exception as e:
        printer_dc.EndDoc()
        printer_dc.DeleteDC()
        win32print.ClosePrinter(printer_handle)
        return False, f"StartPage failed: {e}"

    try:
        # Set font and print message
        printer_dc.SetTextColor(win32api.RGB(0, 0, 0))  # Black text
        printer_dc.SetBkMode(win32con.TRANSPARENT)      # Transparent background
        font = win32ui.CreateFont({
            "name": "Arial",
            "height": 20,
            "weight": win32con.FW_NORMAL,
        })
        printer_dc.SelectObject(font)
        printer_dc.TextOut(100, 100, message)
    except Exception as e:
        printer_dc.EndPage()
        printer_dc.EndDoc()
        printer_dc.DeleteDC()
        win32print.ClosePrinter(printer_handle)
        return False, f"TextOut failed: {e}"

    try:
        # End the page and the document
        printer_dc.EndPage()
        printer_dc.EndDoc()
        printer_dc.DeleteDC()
        win32print.ClosePrinter(printer_handle)
    except Exception as e:
        return False, f"EndPage/EndDoc/DeleteDC/ClosePrinter failed: {e}"

    return True, None
