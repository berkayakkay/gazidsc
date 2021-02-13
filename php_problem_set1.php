<?php
Function SaatCevir($saat){ 
return date(“H:i”, strtotime($saat)); 
}

$suan = date(H:i);
$mesaj = “”;
İf($suan > SaatCevir(“06:00”) and $suan < SaatCevir(“10:00”)){
	$mesaj = “Günaydın”;
}else İf($suan > SaatCevir(“10:00”) and $suan < SaatCevir(“17:00”)){
	$mesaj = “İyi Günler”;
} else İf($suan > SaatCevir(“17:00”) and $suan < SaatCevir(“20:00”)){
	$mesaj = “İyi Akşamlar”;
} else İf($suan > SaatCevir(“20:00”) and $suan < SaatCevir(“00:00”)){
	$mesaj = “İyi Geceler”;
}else{
$mesaj = “Esenlikler Dilerim”;
}
echo $mesaj;
?>