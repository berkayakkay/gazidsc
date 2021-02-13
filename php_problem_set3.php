<?php
function KontrolEt($sayi){
	$toplam =
	$x = 1;
	$say = 0;
	while($sayi >= $x){
		$mod = $sayi % $x;
		İf($mod == 0) $say++;
$x++;
} 
İf($say == 2) $sonuc = “Girilen Sayı Bir Asal Sayı’dır.”;
Else $sonuc = “Girilen Sayı Bir Asal Sayı Değildir.”;

return $sonuc;
}

İf($_POST){
$sayi = $_POST[“sayi”];
İf(is_numeric($sayi) and $sayi > 0){ 
	$sonuc = KontrolEt($sayi);
}else{
	$sonuc = “Hatalı Giriş”;
}
echo ‘<script>alert(“’. $sonuc .’”);</script>’;
}
?>
<form action=”” method=”post” name=”frm_supersayi”>
<input type=”text” name=”sayi” maxlength=”5”><input type=”submit” name=”btn_kontrol” value=”Kontrol Et”>
</form>