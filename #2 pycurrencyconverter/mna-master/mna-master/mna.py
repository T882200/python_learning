#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Mna - A Currency Converter program
# Copyright (c) 2012-2015, Petros Kyladitis <http://www.multipetros.gr/>
# This is free software, distributed under the FreeBSD Lisence

import wx
import webbrowser
import configparser
from wx.lib.wordwrap import wordwrap
from urllib.request import urlopen
from sys import platform
from os.path import expanduser
from os import getenv

class MainFrame(wx.Frame):

    def __init__(self, *args, **kwds):
        # All GCalc API supported currencies
        currencies=["Afghan Afghani (AFN)", "Albanian Lek (ALL)", "Algerian Dinar (DZD)", "Angolan Kwanza (AOA)", "Argentine Peso (ARS)", "Armenian Dram (AMD)", "Aruban Florin (AWG)", "Australian Dollar (AUD)", "Azerbaijani Manat (AZN)", "Bahamian Dollar (BSD)", "Bahraini Dinar (BHD)", "Bangladeshi Taka (BDT)", "Barbadian Dollar (BBD)", "Belarusian Ruble (BYR)", "Belize Dollar (BZD)", "Bermudan Dollar (BMD)", "Bhutanese Ngultrum (BTN)", "Bitcoin (BTC)", "Bolivian Boliviano (BOB)", "Bosnia-Herzegovina Convertible Mark (BAM)", "Botswanan Pula (BWP)", "Brazilian Real (BRL)", "British Pound (GBP)", "Brunei Dollar (BND)", "Bulgarian Lev (BGN)", "Burundian Franc (BIF)", "Cambodian Riel (KHR)", "Canadian Dollar (CAD)", "Cape Verdean Escudo (CVE)", "Cayman Islands Dollar (KYD)", "Central African CFA Franc (XAF)", "CFP Franc (XPF)", "Chilean Peso (CLP)", "Chilean Unit of Account (CLF)", "Chinese Yuan (CNY)", "CNH (CNH)", "Colombian Peso (COP)", "Comorian Franc (KMF)", "Congolese Franc (CDF)", "Costa Rican Colon (CRC)", "Croatian Kuna (HRK)", "Cuban Peso (CUP)", "Czech Republic Koruna (CZK)", "Danish Krone (DKK)", "Djiboutian Franc (DJF)", "Dominican Peso (DOP)", "East Caribbean Dollar (XCD)", "Egyptian Pound (EGP)", "Eritrean Nakfa (ERN)", "Ethiopian Birr (ETB)", "Euro (EUR)", "Falkland Islands Pound (FKP)", "Fijian Dollar (FJD)", "FYROM Denar (MKD)", "Gambian Dalasi (GMD)", "Georgian Lari (GEL)", "Ghanaian Cedi (GHS)", "Gibraltar Pound (GIP)", "Guatemalan Quetzal (GTQ)", "Guinean Franc (GNF)", "Guyanaese Dollar (GYD)", "Haitian Gourde (HTG)", "Honduran Lempira (HNL)", "Hong Kong Dollar (HKD)", "Hungarian Forint (HUF)", "Icelandic Krona (ISK)", "Indian Rupee (INR)", "Indonesian Rupiah (IDR)", "Iranian Rial (IRR)", "Iraqi Dinar (IQD)", "Israeli New Sheqel (ILS)", "Jamaican Dollar (JMD)", "Japanese Yen (JPY)", "Jordanian Dinar (JOD)", "Kazakhstani Tenge (KZT)", "Kenyan Shilling (KES)", "Kuwaiti Dinar (KWD)", "Kyrgystani Som (KGS)", "Laotian Kip (LAK)", "Lebanese Pound (LBP)", "Lesotho Loti (LSL)", "Liberian Dollar (LRD)", "Libyan Dinar (LYD)", "Macanese Pataca (MOP)", "Malagasy Ariary (MGA)", "Malawian Kwacha (MWK)", "Malaysian Ringgit (MYR)", "Maldivian Rufiyaa (MVR)", "Mauritanian Ouguiya (MRO)", "Mauritian Rupee (MUR)", "Mexican Peso (MXN)", "Moldovan Leu (MDL)", "Mongolian Tugrik (MNT)", "Moroccan Dirham (MAD)", "Mozambican Metical (MZN)", "Myanmar Kyat (MMK)", "Namibian Dollar (NAD)", "Nepalese Rupee (NPR)", "Netherlands Antillean Guilder (ANG)", "New Taiwan Dollar (TWD)", "New Zealand Dollar (NZD)", "Nicaraguan Cordoba (NIO)", "Nigerian Naira (NGN)", "North Korean Won (KPW)", "Norwegian Krone (NOK)", "Omani Rial (OMR)", "Pakistani Rupee (PKR)", "Panamanian Balboa (PAB)", "Papua New Guinean Kina (PGK)", "Paraguayan Guarani (PYG)", "Peruvian Nuevo Sol (PEN)", "Philippine Peso (PHP)", "PKG (PKG)", "Polish Zloty (PLN)", "Qatari Rial (QAR)", "Romanian Leu (RON)", "Russian Ruble (RUB)", "Rwandan Franc (RWF)", "Salvadoran Colon (SVC)", "Samoan Tala (WST)", "Sao Tome & Principe Dobra (STD)", "Saudi Riyal (SAR)", "Serbian Dinar (RSD)", "Seychellois Rupee (SCR)", "Sierra Leonean Leone (SLL)", "Singapore Dollar (SGD)", "Solomon Islands Dollar (SBD)", "Somali Shilling (SOS)", "South African Rand (ZAR)", "South Korean Won (KRW)", "Special Drawing Rights (XDR)", "Sri Lankan Rupee (LKR)", "St. Helena Pound (SHP)", "Sudanese Pound (SDG)", "Surinamese Dollar (SRD)", "Swazi Lilangeni (SZL)", "Swedish Krona (SEK)", "Swiss Franc (CHF)", "Syrian Pound (SYP)", "Tajikistani Somoni (TJS)", "Tanzanian Shilling (TZS)", "Thai Baht (THB)", "Tongan Paanga (TOP)", "Trinidad & Tobago Dollar (TTD)", "Tunisian Dinar (TND)", "Turkish Lira (TRY)", "Turkmenistani Manat (TMT)", "Ugandan Shilling (UGX)", "Ukrainian Hryvnia (UAH)", "United Arab Emirates Dirham (AED)", "Uruguayan Peso (UYU)", "US Dollar (USD)", "Uzbekistani Som (UZS)", "Vanuatu Vatu (VUV)", "Venezuelan Bolivar (VEF)", "Vietnamese Dong (VND)", "West African CFA Franc (XOF)", "Yemeni Rial (YER)", "Zambian Kwacha (ZMW)", "Zimbabwean Dollar (ZWL)"]

        # General constants
        self.PRODUCT = "Mna"
        self.VERSION = "1.5.1"

        # Ini path, section, parameters
        if platform == "win32":
            self.INI_FILE = getenv('APPDATA') + "\\mna.cfg"
        else:
            self.INI_FILE = expanduser("~/.mna.cfg")
        self.INI_SECTION = "main"
        self.INI_PARAM_FROM = "from"
        self.INI_PARAM_TO = "to"
        self.INI_PARAM_PRECISION = "precision"

        # Initialize variables that determinate the need of retrieve fresh data from the network
        self.current_currency = 0   # the current curenncies exchange rate
        self.last_from = ""         # the last selected 'from' currency
        self.last_to = ""           # the last selected 'to' currency

        kwds["style"] = wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.TAB_TRAVERSAL | wx.CLIP_CHILDREN | wx.RESIZE_BORDER
        wx.Frame.__init__(self, *args, **kwds)

        # Main frame controls
        self.label_from = wx.StaticText(self, -1, "From")
        self.combo_box_from = wx.ComboBox(self, -1, choices=currencies, style=wx.CB_DROPDOWN | wx.CB_DROPDOWN | wx.CB_READONLY | wx.CB_SORT)
        self.combo_box_from.SetToolTip(wx.ToolTip("Select the currency you want to convert from"))
        self.text_ctrl_from = wx.TextCtrl(self, -1, "")
        self.text_ctrl_from.SetToolTip(wx.ToolTip("Ammount you want to convert"))
        self.label_to = wx.StaticText(self, -1, "To")
        self.combo_box_to = wx.ComboBox(self, -1, choices=currencies, style=wx.CB_DROPDOWN | wx.CB_DROPDOWN | wx.CB_READONLY)
        self.combo_box_to.SetToolTip(wx.ToolTip("Select the currency you want to convert to"))
        self.text_ctrl_to = wx.TextCtrl(self, -1, "", style=wx.TE_READONLY)
        self.text_ctrl_to.SetToolTip(wx.ToolTip("Converted ammount"))
        self.button_convert = wx.Button(self, -1, "Convert")
        self.button_convert.SetToolTip(wx.ToolTip("Click to convert the ammount to selected currency"))
        self.button_convert.SetDefault()

        # Menu Bar
        self.frame_main_menubar = wx.MenuBar()
        # If NOT run on OSX create a File menu and append an Exit menu item. At OSX is unnecessary because of App Menu
        if platform != "darwin":
            self.menu_file = wx.Menu()
            self.menu_item_exit = wx.MenuItem(self.menu_file, wx.ID_EXIT, "&Exit\tCtrl+Q", "Quit the program", wx.ITEM_NORMAL)
            self.menu_file.AppendItem(self.menu_item_exit)
            self.frame_main_menubar.Append(self.menu_file, "&File")
        self.menu_precision = wx.Menu()
        self.menu_item_two_decs = wx.MenuItem(self.menu_precision, 202, "&2 decimals\tCtrl+2", "Precision with 2 decimal digits", wx.ITEM_RADIO)
        self.menu_precision.AppendItem(self.menu_item_two_decs)
        self.menu_item_four_decs = wx.MenuItem(self.menu_precision, 204, "&4 decimals\tCtrl+4", "Precision with 4 decimal digits", wx.ITEM_RADIO)
        self.menu_precision.AppendItem(self.menu_item_four_decs)
        self.menu_item_six_decs = wx.MenuItem(self.menu_precision, 206, "&6 decimals\tCtrl+6", "Precision with 6 decimal digits", wx.ITEM_RADIO)
        self.menu_precision.AppendItem(self.menu_item_six_decs)
        self.menu_item_eight_decs = wx.MenuItem(self.menu_precision, 208, "&8 decimals\tCtrl+8", "Precision with 8 decimal digits", wx.ITEM_RADIO)
        self.menu_precision.AppendItem(self.menu_item_eight_decs)
        self.frame_main_menubar.Append(self.menu_precision, "&Precision")
        self.menu_help = wx.Menu()
        self.menu_item_updates = wx.MenuItem(self.menu_help, wx.NewId(), "&Check for updates\tCtrl+U", "Check if newer versions exist", wx.ITEM_NORMAL)
        self.menu_help.AppendItem(self.menu_item_updates)
        self.menu_item_about = wx.MenuItem(self.menu_help, wx.ID_ABOUT, "&About\tF1", "Show about info", wx.ITEM_NORMAL)
        self.menu_help.AppendItem(self.menu_item_about)
        self.frame_main_menubar.Append(self.menu_help, "&Help")
        self.SetMenuBar(self.frame_main_menubar)

        # Add status bar
        self.statusbar = self.CreateStatusBar()

        self.__set_properties()
        self.__do_layout()

        # Add event handlers
        self.Bind(wx.EVT_BUTTON, self.OnConvert, self.button_convert)
        self.Bind(wx.EVT_COMBOBOX, self.OnConvert, self.combo_box_from)
        self.Bind(wx.EVT_COMBOBOX, self.OnConvert, self.combo_box_to)
        # If NOT run on OSX bind handler for Exit menu item
        if platform != "darwin":
            self.Bind(wx.EVT_MENU, self.OnExit, self.menu_item_exit)
        self.Bind(wx.EVT_CLOSE, self.OnExit)
        self.Bind(wx.EVT_MENU, self.OnPrecisionChange, self.menu_item_two_decs)
        self.Bind(wx.EVT_MENU, self.OnPrecisionChange, self.menu_item_four_decs)
        self.Bind(wx.EVT_MENU, self.OnPrecisionChange, self.menu_item_six_decs)
        self.Bind(wx.EVT_MENU, self.OnPrecisionChange, self.menu_item_eight_decs)
        self.Bind(wx.EVT_MENU, self.OnUpdates, self.menu_item_updates)
        self.Bind(wx.EVT_MENU, self.OnAbout, self.menu_item_about)
        # Bind event handler for double click on status bar
        self.statusbar.Bind(wx.EVT_LEFT_DCLICK, self.OnDblClickStatus, self.statusbar)


    def __set_properties(self):
        self.SetTitle("Mna Currency Converter")
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DFACE))

        # Application icon
        self.ico = wx.Icon("icon.gif", wx.BITMAP_TYPE_GIF)
        self.SetIcon(self.ico)

        # Load ini parameters and set the selected values at combo boxes
        # If ini or parameters missing, not valid or other error set selected USD and EUR
        try:
            config = ConfigParser.ConfigParser()
            config.read(self.INI_FILE)
            self.current_precision = int(config.get(self.INI_SECTION, self.INI_PARAM_PRECISION))
            self.combo_box_from.SetSelection(long(config.get(self.INI_SECTION, self.INI_PARAM_FROM)))
            self.combo_box_to.SetSelection(long(config.get(self.INI_SECTION, self.INI_PARAM_TO)))
        except:
            self.current_precision = 2
            self.combo_box_from.SetSelection(151)
            self.combo_box_to.SetSelection(22)

        # Start-up values, used to determinate selection changes at the program's exit
        self.init_from = self.combo_box_from.GetCurrentSelection()
        self.init_to = self.combo_box_to.GetCurrentSelection()
        self.init_precision = self.current_precision
        self.SetInitPrecision(self.init_precision)


    def __do_layout(self):
        # Use a vertical box sizer to fit menu bar, grid sizer with controls & status bar
        box_sizer = wx.BoxSizer(wx.VERTICAL)

        # Place controls to a flex grid sizer, with empty cells arround them
        grid_sizer_main = wx.FlexGridSizer(5, 5, 6, 6)
        grid_sizer_main.Add((5, 5), 0, 0, 0)
        grid_sizer_main.Add((5, 5), 0, 0, 0)
        grid_sizer_main.Add((5, 5), 0, 0, 0)
        grid_sizer_main.Add((5, 5), 0, 0, 0)
        grid_sizer_main.Add((5, 5), 0, 0, 0)
        grid_sizer_main.Add((5, 5), 0, 0, 0)
        grid_sizer_main.Add(self.label_from, 0, 0, 0)
        grid_sizer_main.Add(self.combo_box_from, 0, 0, 0)
        grid_sizer_main.Add(self.text_ctrl_from, 0, 0, 0)
        grid_sizer_main.Add((5, 5), 0, 0, 0)
        grid_sizer_main.Add((5, 5), 0, 0, 0)
        grid_sizer_main.Add(self.label_to, 0, 0, 0)
        grid_sizer_main.Add(self.combo_box_to, 0, 0, 0)
        grid_sizer_main.Add(self.text_ctrl_to, 0, 0, 0)
        grid_sizer_main.Add((5, 5), 0, 0, 0)
        grid_sizer_main.Add((5, 5), 0, 0, 0)
        grid_sizer_main.Add((5, 5), 0, 0, 0)
        grid_sizer_main.Add((5, 5), 0, 0, 0)
        grid_sizer_main.Add(self.button_convert, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_main.Add((5, 5), 0, 0, 0)
        grid_sizer_main.Add((5, 5), 0, 0, 0)
        grid_sizer_main.Add((5, 5), 0, 0, 0)
        grid_sizer_main.Add((5, 5), 0, 0, 0)
        grid_sizer_main.Add((5, 5), 0, 0, 0)
        grid_sizer_main.Add((5, 5), 0, 0, 0)

        # Add grid sizer with controls to box sizer and set the box sizer
        # as the sizer for the main frame
        box_sizer.Add(grid_sizer_main, 1, wx.EXPAND, 0)
        self.SetSizerAndFit(box_sizer)
        box_sizer.Fit(self)
        self.Layout()


    def SetInitPrecision(self, precision):
        # Set checked the appropriate menu item, based on precision param
        if precision == 4:
            self.menu_item_four_decs.Check(True)
        elif precision == 6:
            self.menu_item_six_decs.Check(True)
        elif precision == 8:
            self.menu_item_eight_decs.Check(True)
        else:
            self.menu_item_two_decs.Check(True)


    def OnDblClickStatus(self, event):
        # If status bar have text, display it on a text box
        if self.statusbar.StatusText != "":
            wx.MessageBox(self.statusbar.StatusText, "Status info",wx.OK | wx.ICON_INFORMATION)



    def OnExit(self, event):
        # 1st of all hide the main form
        self.Hide()

        # If selected currencies differs from the initial selected
        # try to save to the ini configuration file, on error just exit
        try:
            if (long(self.init_from) != self.combo_box_from.GetCurrentSelection()) or (long(self.init_to) != self.combo_box_to.GetCurrentSelection() or self.init_precision != self.current_precision):
                cfgfile = open(self.INI_FILE,"w")
                config = ConfigParser.ConfigParser()
                config.read(self.INI_FILE)

                # Try to add the main section, if exist an exception will be thrown, in that case resume next
                try:
                    config.add_section(self.INI_SECTION)
                except:
                    pass

                # Set the values to ini parameters and save
                config.set(self.INI_SECTION, self.INI_PARAM_PRECISION, str(self.current_precision))
                config.set(self.INI_SECTION, self.INI_PARAM_FROM, str(self.combo_box_from.GetCurrentSelection()))
                config.set(self.INI_SECTION, self.INI_PARAM_TO, str(self.combo_box_to.GetCurrentSelection()))
                config.write(cfgfile)
                cfgfile.close()
        except:
            pass

        self.Destroy()


    def GetUpdateInfo(self, productName):
        # Retrieve update info from server in the format: x.y.z,url://to.this.version
        # and if new version exist, prompt user to browse to this url, else infom
        # that no new version is available.
        try:
            # Read data from last.ver on the master branch
            # Split retrieved data in 2 parts, 1st is the version, 2nd is the url and
            # set the variables stripped. Then check if new version exist & handle it.
            updateInfo = urlopen("https://raw.githubusercontent.com/multipetros/mna/master/last.ver").read()
            updateInfoArray = updateInfo.split(",",2)
            updateVer = updateInfoArray[0].strip()
            updateUrl = updateInfoArray[1].strip()
            if self.CheckUpdate(self.VERSION, updateVer) == True:
                if platform == "win32":
                    # Because of Windows 7 don't appear question icon, show info icon instead
                    wxIcon =  wx.ICON_INFORMATION
                else:
                    wxIcon = wx.ICON_QUESTION
                answer = wx.MessageBox("You are running " + self.PRODUCT + " version " + self.VERSION + "\nThe updated version " + updateVer + " is available.\nDo you want to visit website for downloading it?", "Update available", wx.YES_NO | wx.YES_DEFAULT | wxIcon)
                if answer == wx.YES:
                    webbrowser.open_new(updateUrl)
                else:
                    return
            else:
                wx.MessageBox("There are no updates available. It seems you running the latest version", "No update", wx.OK | wx.ICON_INFORMATION)
        except Exception as details:
            wx.MessageBox("Can't retrieve update info because of: " + str(details), "Error", wx.OK | wx.ICON_ERROR)


    def CheckUpdate(self, currentVer, serverVer):
        # From curent version string and server version string, formated
        # as x.y.z (major.minor.revision), check any new version exist
        currentVersionArray = currentVer.split(".",3)
        serverVersionArray = serverVer.split(".",3)
        try:
               currentMajor = int(currentVersionArray[0])
               currentMinor = int(currentVersionArray[1])
               currentRevision = int(currentVersionArray[2])
               serverMajor = int(serverVersionArray[0])
               serverMinor = int(serverVersionArray[1])
               serverRevision = int(serverVersionArray[2])
        except:
           return False
        if serverMajor > currentMajor:
           return True
        elif serverMajor == currentMajor and serverMinor > currentMinor:
           return True
        elif serverMajor == currentMajor and serverMinor == currentMinor and serverRevision > currentRevision:
           return True
        else:
           return False

    def OnUpdates(self, event):
        #Determinate if any update exist and handle it
        self.GetUpdateInfo(self.PRODUCT)


    def OnAbout(self, event):
        # create and show an about dialog box
        info = wx.AboutDialogInfo()
        info.SetName("Mna Currency Converter")
        info.SetVersion(self.VERSION)
        info.SetCopyright("Copyright (C) 2012-2015, Petros Kyladitis")
        info.Description = wordwrap("A currency converter program for Python, using wxPython for the GUI and urllib2 library with Google Finance service to retrieve updated exchange data.", 350, wx.ClientDC(self))
        info.SetWebSite("http://www.multipetros.gr")
        info.License = wordwrap("This program is free software, distributed under the terms and conditions of the FreeBSD License. For full licensing info see the \"license.txt\" file, distributed with this program", 350, wx.ClientDC(self))
        info.SetIcon(self.ico) # Declared at self.__set_properties()
        wx.AboutBox(info)


    def OnPrecisionChange(self, event):
        # Get the id of the menu item that raise the event. The ids are especially setted
        # as (item meaning + 200), so it's easy to find the selected precision value
        self.current_precision = event.GetId() - 200
        self.DoConvertion(False)


    def OnConvert(self, event):
        # If the current selected currencies is the same as the last convertion,
        # start the convertion without retrieve fresh data, else convert with  retriving new data
        # and save the selected curencies values as the last selected.
        if (self.combo_box_from.Value == self.last_from) and (self.combo_box_to.Value == self.last_to):
            self.DoConvertion(False)
        else:
            self.DoConvertion()
            self.last_from = self.combo_box_from.Value
            self.last_to = self.combo_box_to.Value


    def DoConvertion(self, retrieveFreshData=True):

        # Try to convert the user inputed amount into a float, on error set it to 1.0
        try:
            user_input_ammount = float(self.text_ctrl_from.Value)
        except:
            user_input_ammount = 1.0
            self.text_ctrl_from.Value = str(user_input_ammount)

        # Convert if negative ammount to absolute value
        if user_input_ammount < 0:
            user_input_ammount = -1 * user_input_ammount
            self.text_ctrl_from.Value = str(user_input_ammount)

        if (retrieveFreshData == True) or (self.current_currency == 0):
            # Parse the 3-letter international name of selected currencies, which are
            # inside of the parentheses "name of cur (xxx)" of selected combo box values
            from_cur_name = self.combo_box_from.Value[(self.combo_box_from.Value.find("(")+1):self.combo_box_from.Value.find(")")]
            to_cur_name = self.combo_box_to.Value[(self.combo_box_to.Value.find("(")+1):self.combo_box_to.Value.find(")")]

            # Read the returned data from the Google Fiance service, when passing the above cur names
            # in the returned page the converter string looks like "<span class=bld>123 CUR</span>"
            # or no "<span class=bld>" element exist, but a "Could not convert" string.
            # So, try to find the "<span class=bld>" node, parse the value after that and use it to
            #calculate the result. Or error, show the exception message to the status bar.
            try:
                self.SetStatusText("Retrieving data. Please wait...")
                gcalc_currency = urlopen("http://www.google.com/finance/converter?a=1&from=" + from_cur_name + "&to=" + to_cur_name).read()
                start_str = "<span class=bld>"
                gcalc_currency_start = gcalc_currency.find(start_str) + len(start_str)
                #if no connection error, but Google Finance could not convert this
                if(gcalc_currency_start-len(start_str) == -1):
                    cant_convertion_msg = gcalc_currency.find("Could not convert")
                    if(cant_convertion_msg != -1):
                        self.SetStatusText("Google Finance, could not convert this.")
                        self.current_currency = 0 # To force retrieve data at the next DoConvertion(False) callr
                        return
                gcalc_currency_end = gcalc_currency.find(" ", gcalc_currency_start)
                self.current_currency = float(gcalc_currency[gcalc_currency_start:gcalc_currency_end])
                self.SetStatusText("Exchange rate: 1 " + from_cur_name + " = " + str(self.current_currency) + " " + to_cur_name)
            except Exception as details:
                self.SetStatusText("Can\'t retrieve data from Google Finance. " + str(details))
                self.current_currency = 0 # To force retrieve data at the next DoConvertion(False) call
                return

        result =  user_input_ammount * self.current_currency
        self.text_ctrl_to.Value = str(round(result,self.current_precision))

# end of class MainFrame


class MnaApp(wx.App):
    # Override method for handling kAEReopenApplication to work correctly with the Dock at OSX
    def MacReopenApp(self):
        try:
            self.GetTopWindow().Raise()
        except:
            pass


if __name__ == "__main__":
    app = MnaApp(False)
    frame_main = MainFrame(None, -1, "")
    app.SetTopWindow(frame_main)
    frame_main.Show()
    app.MainLoop()
