/* The javascript files that contain the control functions for the flow definition page */

block_ht = function (num){

	return "<div id = \"block_"+num+"\" class = \"container\" style = \" background-color : rgb(192,0,192); width : 240px ; height: 240px \"><p  class = \"btn btn-default text-info\" > Test Block "+num+" </p></div>";

}



fl_block = function(num){
	
	str = "<div id=\"block_del_"+num+"\" class=\"container\"style=\"width: 300px; height: 150px; background: url('f_ar.png'); opacity: 0.5;\"><button id = 'load' class = 'btn btn-primary' style='position : relative; top : 85px; left: 248px;'><b>&gt;	<b></button><button class=\"btn btn-danger\" id=\"del_"+num+"\" style=\"position : relative; top : 1px; left : 248px;\"><b>X</b></button><input type='file' id = 'file_in_"+num+"' style= 'visibility: hidden;'></input><div class=\"row\"><div class=\"col-sm-3\"style=\"position: relative; top: 10px; left: 100px;\"><span class=\"btn btn-success btn-file\" onclick='console.log(\"fuck\"); $(\"#file_in_"+num+"\").click();'> Browse </span></div></div>	</div>";
	
	return str;
	
}

pp_block = function(num) {
	
	return "<div id=\"block_del_"+num+"\" class=\"container\"style=\"width: 300px; height: 150px; background: url('f_ar.png'); opacity: 0.5;\"><button class=\"btn btn-danger\" id=\"del_"+num+"\" style=\"position : relative; top : 1px; left : 248px;\"><b>X</b></button> <input type='file' id = 'file_in"+num+"' style= 'visibility: hidden;'></input><div class=\"row\"><div class=\"col-sm-3\"style=\"position: relative; top: 10px; left: 100px;\"><span class=\"btn btn-success btn-file\" onclick='console.log(\"fuck\"); $(\"#file_in"+num+"\").click();'> Browse <inputtype=\"file\"></span></div></div>	</div>";
	
	
}

des_block = function(num) {

    str = "<div id = 'des_"+num+"' class=\"container\"style=\"width : 640px; height: 400px; background-color : rgba(192,192,192,0.75);\"> OK </div>";
    return str;
}

//var profile = "<div class=\"container\" style=\"width:300px; height:150px; 		background: url('f_ar.png'); opacity : 0.5 ;\"><div class=\"row\"></div></div>";

//var block_ht= "<div id = \"block\" class = \"container\" style = \" background-color : rgb(192,0,192); width : 240px ; height: 240px \"><p  class = \"btn btn-default text-info\" > Test Block </p></div>";

