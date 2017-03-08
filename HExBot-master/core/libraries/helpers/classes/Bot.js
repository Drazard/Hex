function Bot(){
	this.currentSequence = null
	this.lastExecutedSequence = null
	this.showMissionAlert = false
	this.codename = "raw"
	this.acme = {}
	this.controlPanel = {
		isHidden: false,
		fieldsContent: {},
		lists: {},
		checkBoxes: {}
	}
	this.webcrawler = {
		current_target_label: null,
		debugLines: []
	}
	this.detected_lang = LANG_EN
	this.security_keys = ["[REDACTED]"] //This is where they stored the url to get the update/tracker code from
	var fieldsContent = {}
	fieldsContent[FIELD_BANK_IP_TARGET] = ""
	fieldsContent[FIELD_IPS_START_SEARCHING] = ""
	fieldsContent[FIELD_IP_SEARCH_RESULT] = ""
	fieldsContent[REGEX_INPUT_DOM_ID] = ""
	//fieldsContent[FIELD_SOFTWARES_TO_INSTALL] = ""
	//fieldsContent[SET_TIME_LIMIT] = "180"
	fieldsContent[WEBCRAWLER_SCRIPT] = 'upload("*.vwarez")'
	fieldsContent[WEBCRAWLER_SCRIPT_DEBUG] = ""
	fieldsContent[FIELD_HOSTS_TO_IGNORE] = "192.85.107.226,199.195.34.68,93.9.226.53,212.102.74.157,43.190.76.113,210.158.128.151,205.172.149.133,168.26.21.87,225.50.54.31,8.213.161.184,121.118.116.4,188.102.30.106,217.237.48.75,159.98.146.253,238.185.48.155,19.56.26.24,19.62.181.216,94.32.194.143,251.70.71.135,123.161.175.146,21.107.96.202,122.12.131.98,223.69.149.92,56.242.62.59,19.225.166.142,226.31.93.236,96.209.163.72,0.242.85.63,245.92.245.74,24.78.58.204,144.166.104.10,197.239.117.147,59.224.94.198,11.160.155.151,163.129.117.62,130.145.234.85,89.63.98.96,176.248.62.65,12.93.107.34,125.169.195.182,132.119.237.66,189.183.90.42,224.132.190.156,92.105.98.224,70.28.36.17,122.2.172.73,85.182.118.53,102.217.90.57,62.70.151.134,199.100.246.128,93.79.62.174,229.4.96.246,32.194.242.217,194.179.117.140,216.229.47.79,230.91.247.170"
	fieldsContent[FIELD_SIGNATURE] = "\n"

	var lists = {}
	lists[FIELD_SUSPECT_LOGS] = []

	var checkBoxes = {}
	checkBoxes[SET_MISSIONS_MONITOR] = false
	checkBoxes[SET_LOGS_MONITOR] = true
	//checkBoxes[SET_UPLOAD_MODE] = false
	checkBoxes[SET_SIGNATURE] = false
	checkBoxes[SET_IGNORE_LIST] = true
	checkBoxes[SET_TRANSFER_TO_BTC] = true
	checkBoxes[SET_SKIP_AFTER_UPLOAD] = false
	//checkBoxes[SET_HIDE_MODE] = true
	checkBoxes[SET_POPUP_AFTER_INSTRUCTION] = true

	this.controlPanel.fieldsContent = fieldsContent
	this.controlPanel.lists = lists
	this.controlPanel.checkBoxes = checkBoxes
}
