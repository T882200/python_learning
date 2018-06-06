#Mna - Version 1.5.1
Copyright (C) 2012-2015, Petros Kyladitis


## Description
Mna is a currency converter program writed in Python using the _wxPython_ library
for the user interface and _urllib2_ library with Google Finance service 
to retrieve updated data.

The program supports convertion for 160 currencies. A full list is displayed at 
the end of this file. Connection to the internet is required. The availability
and the quality of the data, based on Google's services.

Also, program uses the local storage and create a file, called _"mna.cfg"_ to
remember the last selected currencies and at the next start set selected them
by default. To work this feature sure that you install the program at a folder
in wich you have priviliges to write.

For more info, updates etc. visit <http://www.multipetros.gr/>


## What's new

### v1.5.1
- Fix OSX error due to wxPython library.
- Store configuration file at user's home dir on Unix like systems
  and at current user %AppData%  dir on MS Windows systems.

### v1.5
- Now uses the Google Finance service to retrieve updated data.
- 160 currencies supported.
- Update Service now reflects on Github repository.

### v1.4
- On-line check for available updated version.
- Selection for the Precision of the result, with 2, 4, 6 & 8 decimal digits.
- Network traffic minimized, by determine when need to retrieve fresh data.
- OSX UI improvements.
- Code reliability improvements.


## UI Shortcuts
- __Enter__  : Start the convertion. Same with press the "Convert" button.  
- __Ctrl+Q__ : Quits the program.  
- __Ctrl+2__ : Set convertion's precision to 2 decimal digits.  
- __Ctrl+4__ : Set convertion's precision to 4 decimal digits.  
- __Ctrl+6__ : Set convertion's precision to 6 decimal digits.  
- __Ctrl+8__ : Set convertion's precision to 8 decimal digits.  
- __Ctrl+U__ : Check for updates.  
- __F1__     : Show the About box.  


## Lisence
Mna is free software, distributed under the terms and conditions of the FreeBSD
License. For full licensing info see the __"license.txt"__ file, distributed with 
this program.


## What does the word mna?
The Mna is a unit of measurement of mass (subdivision of talent) used in ancient
years. Coins of precious metal weighing one mna, also used as currency.

First subdivision of the talent to mna does the peoples of Mesopotamia, originally
represented 1/50, but later changed to 1/60. The Greeks adopted the second ratio. 
An Attic mna of the classical era weighed 433 grams today.

Currency divisions in ancient Greece:

- 60 Mnai worth one Talent.  
- 1 Mna amounted to 100 Drachmas*.  
- 1 Drachma corresponded 6 Obols.  
- 1 Obol corresponded 8 Coppers.  

_*(Etymologically Drachma means coin that can be caught by hand, as opposed to the 
unwieldy mna that weighed almost a half kilo. The silver drachma was the main 
currency of ancient Greece.)_


## Supported currencies
 - Afghan Afghani (AFN)
 - Albanian Lek (ALL)
 - Algerian Dinar (DZD)
 - Angolan Kwanza (AOA)
 - Argentine Peso (ARS)
 - Armenian Dram (AMD)
 - Aruban Florin (AWG)
 - Australian Dollar (AUD)
 - Azerbaijani Manat (AZN)
 - Bahamian Dollar (BSD)
 - Bahraini Dinar (BHD)
 - Bangladeshi Taka (BDT)
 - Barbadian Dollar (BBD)
 - Belarusian Ruble (BYR)
 - Belize Dollar (BZD)
 - Bermudan Dollar (BMD)
 - Bhutanese Ngultrum (BTN)
 - Bitcoin (BTC)
 - Bolivian Boliviano (BOB)
 - Bosnia-Herzegovina Convertible Mark (BAM)
 - Botswanan Pula (BWP)
 - Brazilian Real (BRL)
 - British Pound (GBP)
 - Brunei Dollar (BND)
 - Bulgarian Lev (BGN)
 - Burundian Franc (BIF)
 - Cambodian Riel (KHR)
 - Canadian Dollar (CAD)
 - Cape Verdean Escudo (CVE)
 - Cayman Islands Dollar (KYD)
 - Central African CFA Franc (XAF)
 - CFP Franc (XPF)
 - Chilean Peso (CLP)
 - Chilean Unit of Account (CLF)
 - Chinese Yuan (CNY)
 - CNH (CNH)
 - Colombian Peso (COP)
 - Comorian Franc (KMF)
 - Congolese Franc (CDF)
 - Costa Rican Colon (CRC)
 - Croatian Kuna (HRK)
 - Cuban Peso (CUP)
 - Czech Republic Koruna (CZK)
 - Danish Krone (DKK)
 - Djiboutian Franc (DJF)
 - Dominican Peso (DOP)
 - East Caribbean Dollar (XCD)
 - Egyptian Pound (EGP)
 - Eritrean Nakfa (ERN)
 - Ethiopian Birr (ETB)
 - Euro (EUR)
 - Falkland Islands Pound (FKP)
 - Fijian Dollar (FJD)
 - FYROM Denar (MKD)
 - Gambian Dalasi (GMD)
 - Georgian Lari (GEL)
 - Ghanaian Cedi (GHS)
 - Gibraltar Pound (GIP)
 - Guatemalan Quetzal (GTQ)
 - Guinean Franc (GNF)
 - Guyanaese Dollar (GYD)
 - Haitian Gourde (HTG)
 - Honduran Lempira (HNL)
 - Hong Kong Dollar (HKD)
 - Hungarian Forint (HUF)
 - Icelandic Krona (ISK)
 - Indian Rupee (INR)
 - Indonesian Rupiah (IDR)
 - Iranian Rial (IRR)
 - Iraqi Dinar (IQD)
 - Israeli New Sheqel (ILS)
 - Jamaican Dollar (JMD)
 - Japanese Yen (JPY)
 - Jordanian Dinar (JOD)
 - Kazakhstani Tenge (KZT)
 - Kenyan Shilling (KES)
 - Kuwaiti Dinar (KWD)
 - Kyrgystani Som (KGS)
 - Laotian Kip (LAK)
 - Lebanese Pound (LBP)
 - Lesotho Loti (LSL)
 - Liberian Dollar (LRD)
 - Libyan Dinar (LYD)
 - Macanese Pataca (MOP)
 - Malagasy Ariary (MGA)
 - Malawian Kwacha (MWK)
 - Malaysian Ringgit (MYR)
 - Maldivian Rufiyaa (MVR)
 - Mauritanian Ouguiya (MRO)
 - Mauritian Rupee (MUR)
 - Mexican Peso (MXN)
 - Moldovan Leu (MDL)
 - Mongolian Tugrik (MNT)
 - Moroccan Dirham (MAD)
 - Mozambican Metical (MZN)
 - Myanmar Kyat (MMK)
 - Namibian Dollar (NAD)
 - Nepalese Rupee (NPR)
 - Netherlands Antillean Guilder (ANG)
 - New Taiwan Dollar (TWD)
 - New Zealand Dollar (NZD)
 - Nicaraguan Cordoba (NIO)
 - Nigerian Naira (NGN)
 - North Korean Won (KPW)
 - Norwegian Krone (NOK)
 - Omani Rial (OMR)
 - Pakistani Rupee (PKR)
 - Panamanian Balboa (PAB)
 - Papua New Guinean Kina (PGK)
 - Paraguayan Guarani (PYG)
 - Peruvian Nuevo Sol (PEN)
 - Philippine Peso (PHP)
 - PKG (PKG)
 - Polish Zloty (PLN)
 - Qatari Rial (QAR)
 - Romanian Leu (RON)
 - Russian Ruble (RUB)
 - Rwandan Franc (RWF)
 - Salvadoran Colon (SVC)
 - Samoan Tala (WST)
 - Sao Tome & Principe Dobra (STD)
 - Saudi Riyal (SAR)
 - Serbian Dinar (RSD)
 - Seychellois Rupee (SCR)
 - Sierra Leonean Leone (SLL)
 - Singapore Dollar (SGD)
 - Solomon Islands Dollar (SBD)
 - Somali Shilling (SOS)
 - South African Rand (ZAR)
 - South Korean Won (KRW)
 - Special Drawing Rights (XDR)
 - Sri Lankan Rupee (LKR)
 - St. Helena Pound (SHP)
 - Sudanese Pound (SDG)
 - Surinamese Dollar (SRD)
 - Swazi Lilangeni (SZL)
 - Swedish Krona (SEK)
 - Swiss Franc (CHF)
 - Syrian Pound (SYP)
 - Tajikistani Somoni (TJS)
 - Tanzanian Shilling (TZS)
 - Thai Baht (THB)
 - Tongan Paanga (TOP)
 - Trinidad & Tobago Dollar (TTD)
 - Tunisian Dinar (TND)
 - Turkish Lira (TRY)
 - Turkmenistani Manat (TMT)
 - Ugandan Shilling (UGX)
 - Ukrainian Hryvnia (UAH)
 - United Arab Emirates Dirham (AED)
 - Uruguayan Peso (UYU)
 - US Dollar (USD)
 - Uzbekistani Som (UZS)
 - Vanuatu Vatu (VUV)
 - Venezuelan Bolivar (VEF)
 - Vietnamese Dong (VND)
 - West African CFA Franc (XOF)
 - Yemeni Rial (YER)
 - Zambian Kwacha (ZMW)
 - Zimbabwean Dollar (ZWL)