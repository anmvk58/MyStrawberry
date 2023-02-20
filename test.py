if __name__ == '__main__':
    string = "372237303736373837373729370637213711 3716375037473751375937553775378137763774377337393780378337 84"
    string = string.replace(" ", "")
    string = string.replace("một", "1")
    string = string.replace("hai", "2")
    string = string.replace("ba", "3")
    string = string.replace("bốn", "4")
    string = string.replace("năm", "5")
    string = string.replace("sáu", "6")
    string = string.replace("bảy", "7")
    string = string.replace("tám", "8")
    string = string.replace("chín", "9")
    string = string.replace("mươi", "0")
    n = 4
    for i in range(0, len(string), n):
        print(string[i:i + n])