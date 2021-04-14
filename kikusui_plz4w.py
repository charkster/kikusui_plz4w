import time

# https://manual.kikusui.co.jp/P/PLZ4W/i_f_manual/english/00-intro.html
class kikusui_plz4w():

    def __init__(self, pyvisa_instr):
        self.plz4w = pyvisa_instr  # this is the pyvisa instrument, rm.open_resource('USB0::0x0A7E::0x1205::VB011286::INSTR')

    def get_all_scpi_list(self):
        result_list = [ ]
        for dict in [self.source_dict, self.inout_dict, self.meas_trig_dict ]:
            for command in dict:
                time.sleep(0.1)
                # print(command.format("?"))
                result = (self.plz4w.query(command.format("?"))).rstrip('\r\n')
                result = " " + result
                result_list.append(command.format(result))
                # print(command.format(result))
        return result_list

    def get_unique_scpi_list(self):
        unique_scpi_list = []
        inst_settings_list = self.get_all_scpi_list()
        for setting in inst_settings_list:
            if (setting not in self.settings_por_scpi_list):
                unique_scpi_list.append(setting)
        return unique_scpi_list

    source_dict = {"SOURce:CONDuctance{0}": "Set the conductance",
                   "SOURce:CONDuctance:RANGe{0}": "Set the range of conductance",
#                   "SOURce:CONDuctance:TRIGgered{0}": "Set the conductance when a trigger is activated",
                   "SOURce:CURRent{0}": "Set the current",
                   "SOURce:CURRent:PROTection{0}": "Set the overcurrent protection",
                   "SOURce:CURRent:PROTection:ACTion{0}": "Sets whether to turn off the load or limit the current when the OCP trips",
                   "SOURce:CURRent:RANGe{0}": "Set the range of current",
                   "SOURce:CURRent:SLEW{0}": "Set the slew rate",
#                   "SOURce:CURRent:TRIGgered{0}": "Set the current when a trigger is activated",
                   "SOURce:FUNCtion{0}": "Sets the operation mode",
                   "SOURce:FUNCtion:CTIMe{0}": "Turns ON/OFF the count time",
                   "SOURce:FUNCtion:RESPonse{0}": "Set the transient response speed",
#                   "SOURce:FUNCution:RESPonse:CR{0}": "Set the transient response speed for CR mode of PLZ-4WL",
#                   "SOURce:FUNCution:RESPonse:CV{0}": "Set the transient response speed for CV mode of PLZ-4WL",
                   "SOURce:FUNCtion:SSTart{0}": "Set the soft start time",
                   "SOURce:POWer{0}": "Set the power",
                   "SOURce:POWer:PROTection{0}": "Set the overpower protection",
                   "SOURce:POWer:PROTection:ACTion{0}": "Sets whether to turn off the load or limit the power when the OPP trips",
                   "SOURce:POWer:RANGe{0}": "Set the range of power",
#                   "SOURce:PRESet:RECall{0}": "Recalls settings from memory",
#                   "SOURce:PRESet:STORe{0}": "Stores the settings to memory",
                   "SOURce:PULSe{0}": "Turns ON/OFF the switching mode",
                   "SOURce:PULSe:DCYCle{0}": "Set the switching duty cycle",
                   "SOURce:PULSe:FREQuency{0}": "Set the pulse frequency",
                   "SOURce:PULSe:LEVel:CONDuctance{0}": "Set the conductance level",
                   "SOURce:PULSe:LEVel:CURRent{0}": "Set the current level",
                   "SOURce:PULSe:LEVel:PERCentage:CONDuctance{0}": "Set the conductance level in terms of a percentage of the setting",
                   "SOURce:PULSe:LEVel:PERCentage:CURRent{0}": "Set the current level in terms of a percentage of the setting",
                   "SOURce:PULSe:PERiod{0}": "Set the pulse period",
                   "SOURce:VOLTage{0}": "Set the voltage",
                   "SOURce:VOLTage:PROTection:STATe{0}": "Turns ON/OFF the undervoltage protection",
                   "SOURce:VOLTage:PROTection:UNDer{0}": "Set the undervoltage protection",
                   "SOURce:VOLTage:RANGe{0}": "Set the range of voltage" }

    inout_dict = { "INPut{0}": "Turns ON/OFF the load",
                   "OUTPut{0}": "Turns ON/OFF the load",
#				   "INPut:PROTection:CLEar{0}"  : "Clears the alarm",
#				   "OUTPut:PROTection:CLEar{0}" : "Clears the alarm",
                   "INPut:SHORt{0}": "Turns ON/OFF the short function",
                   "OUTPut:SHORt{0}": "Turns ON/OFF the short function",
                   "INPut:TIMer{0}": "Set the cutoff time",
                   "OUTPut:TIMer{0}": "Set the cutoff time",
#                   "INPut:TRIGgered{0}": "Turns ON/OFF the load when a trigger is activated",
#                   "OUTPut:TRIGgered{0}": "Turns ON/OFF the load when a trigger is activated"
                   }

    meas_trig_dict = { "INIT:CONT{0}": "Sets whether to continue the trigger wait status",
#	                   "MEASure:CURRent{0}" : "Reads the measured current",
#	                   "MEASure:POWer{0}"   : "Reads the measured power",
#					   "MEASure:VOLTage{0}" : "Reads the measured voltage",
#					   "MEASure:ETIMe{0}"   : "Reads the elapsed time of measurement",
#					   "ABORt"              : "Aborts the trigger function",
#					   "INIT"               : "Initiates the trigger function",
                    }
    system_dict = { "SYSTem:CAPability{0}"   : "Query the SCPI instrument class and the basic functions",
	                "SYSTem:ERRor{0}"        : "Reads the oldest error information",
					"SYSTem:KLOCk"           : "Locks the panel operation for PLZ-4WH",
                    "SYSTem:KLOCk:SELect{0}": "Set the type of panel lock operation for PLZ-4WH",
                    "SYSTem:LOCk{0}": "Set the PLZ-4W/PLZ-4WL/PLZ-4WH operation to panel operation",
                    "SYSTem:REMote{0}": "Set the PLZ-4W/PLZ-4WL/PLZ-4WH operation to remote mode",
                    "SYSTem:RENable{0}": "Set the PLZ-4W operation to remote mode",
                    "SYSTem:RSENsing{0}": "Set the remote sensing function for PLZ-4WL",
                    "SYSTem:RWLock{0}": "Set the PLZ-4W/PLZ-4WL/PLZ-4WH operation to remote mode",
					"SYSTem:VERSion{0}"      : "Query the version of the SCPI specifications" }

    program_dict = { "PROGram:CLEar"          : "Delete the contents of the sequence",
                     "PROGram:CHAin{0}": "Set the number of the program to be executed next",
                     "PROGram:CRANge{0}": "Set the current range",
                     "PROGram:EXECuting{0}": "Query the number of the program currently in operation",
                     "PROGram:FSPeed:EDIT{0}": "Edit an existing step (fast sequence)",
                     "PROGram:FSPeed:EDIT:LINear{0}": "Set the FILL function (fast sequence)",
                     "PROGram:FSPeed:EDIT:WAVE{0}": "Edit the waveform of the step (fast sequence)",
                     "PROGram:FSPeed:END{0}": "Set the end step (fast sequence)",
                     "PROGram:FSPeed:TIME{0}": "Set the step execution time (fast sequence)",
                     "PROGram:LINPut{0}": "Set the load on/off condition after the sequence ends",
                     "PROGram:LOOP{0}": "Set the number of program loops",
                     "PROGram:LOUT{0}": "Set the load on/off condition after the sequence ends",
                     "PROGram:LVALue{0}": "Set the setting value after the specified program ends",
                     "PROGram:MEMO{0}": "Set the memo",
                     "PROGram:MODE{0}": "Set the mode",
                     "PROGram:NAME{0}": "Specify the program number",
                     "PROGram:NSPeed:ADD{0}": "Add a step after the last step (normal sequence)",
                     "PROGram:NSPeed:COUNt{0}": "Query the number of steps (normal sequence)",
                     "PROGram:NSPeed:DELete{0}": "Delete the selected program sequence step (normal sequence)",
                     "PROGram:NSPeed:DELete:ALL": "Deletes the all the steps (normal sequence)",
                     "PROGram:NSPeed:EDIT{0}": "Edit an existing sequence step (normal sequence)",
                     "PROGram:NSPeed:INSert{0}": "Insert a normal sequence step (normal sequence)",
                     "PROGram:STATe{0}": "Execute the selected program",
                     "PROGram:VRANge{0}": "Set the voltage range" }

    status_dict = { "STATus:CSUMmary{0}": "CSUMmary status register: Event",
                    "STATus:CSUMmary:CONDtion{0}": "CSUMmary status register: Condition of register",
                    "STATus:CSUMmary:ENABle{0}": "CSUMmary status register: Enable register",
                    "STATus:CSUMmary:PTRansition{0}": "CSUMmary status register: Positive transition",
                    "STATus:CSUMmary:NTRansition{0}": "CSUMmary status register: Negative transition",
                    "STATus:OPERation{0}": "OPERation status register: Event",
                    "STATus:OPERation:CONDtion{0}": "OPERation status register: Condition of register",
                    "STATus:OPERation:ENABle{0}": "OPERation status register: Enable register",
                    "STATus:OPERation:PTRansition{0}": "OPERation status register: Positive transition",
                    "STATus:OPERation:NTRansition{0}": "OPERation status register: Negative transition",
                    "STATus:QUEStionable{0}": "QUEStionable status register: Event",
                    "STATus:QUEStionable:CONDtion{0}": "QUEStionable status register: Condition of register",
                    "STATus:QUEStionable:ENABle{0}": "QUEStionable status register: Enable register",
                    "STATus:QUEStionable:PTRansition{0}": "QUEStionable status register: Positive transition",
                    "STATus:QUEStionable:NTRansition{0}": "QUEStionable status register: Negative transition",
                    "STATus:PRESet{0}": "Constructing status data"}

    settings_por_scpi_list = [ "SOURce:CURRent:PROTection:ACTion LIM",
                               "SOURce:FUNCtion CC",
                               "SOURce:PULSe:DCYCle 50.0",
                               "SOURce:PULSe:LEVel:PERCentage:CURRent 100.0",
                               "SOURce:VOLTage:PROTection:STATe 0",
                               "SOURce:VOLTage:RANGe HIGH",
                               "SOURce:PULSe:LEVel:CONDuctance 0.000",
                               "SOURce:CURRent 0.000",
                               "SOURce:CURRent:RANGe HIGH",
                               "SOURce:VOLTage 0.00",
                               "SOURce:PULSe:PERiod 0.200000",
                               "SOURce:FUNCtion:RESPonse 1.0",
                               "SOURce:CURRent:PROTection 36.29",
                               "SOURce:PULSe:LEVel:CURRent 0.000",
                               "SOURce:FUNCtion:SSTart 0.001",
                               "SOURce:CURRent:SLEW 0.002500",
                               "SOURce:PULSe:LEVel:PERCentage:CONDuctance 50.0",
                               "SOURce:POWer:RANGe HIGH",
                               "SOURce:PULSe 0",
                               "SOURce:POWer:PROTection 181.5",
                               "SOURce:PULSe:FREQuency 5.0",
                               "SOURce:CONDuctance:RANGe HIGH",
                               "SOURce:CONDuctance 0.0000",
                               "SOURce:POWer 0.00",
                               "SOURce:FUNCtion:CTIMe 0",
                               "SOURce:POWer:PROTection:ACTion LIM",
                               "SOURce:VOLTage:PROTection:UNDer 0.00",
                               "INPut 0",
                               "INPut:SHORt 0",
                               "INPut:TIMer 0",
                               "OUTPut 0",
                               "OUTPut:TIMer 0",
                               "OUTPut:SHORt 0",
                               "INIT:CONT 0" ]
