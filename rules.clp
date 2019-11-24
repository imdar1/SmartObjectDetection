; (defclass )
(defrule isSegitigaTidakBeraturan ""
   (sisi 3)
   =>
   (assert (objek segitigaTidakBeraturan)))

(defrule isSegiEmpatTidakBeraturan ""
   (sisi 4)
   =>
   (assert (objek segiempatTidakBeraturan)))

(defrule isJajaranGenjang ""
  (objek segiempatTidakBeraturan)
  (jumlahSisiSama 2)
  (sudutTumpul 2)
  (sudutLancip 2)
  (sudutSikuSiku 0)
  (jumlahPasanganSejajar 2)
  =>
  (assert (objek jajaranGenjang)))

(defrule isSegiEmpatBeraturan
  (objek segiempatTidakBeraturan)
  (sudutSiku 4)
  (sudutLancip 0)
  (sudutTumpul 0)
  =>
  (assert (objek segiEmpatBeraturan)))

(defrule isLayangLayang
  (objek segiempatTidakBeraturan)
  (sudutSiku 2)
  (sudutLancip 1)
  (sudutTumpul 1)
  (jumlahPasanganSejajar 0)
  =>
  (assert (objek layangLayang)))

(defrule isLayangLayang2
  (objek segiempatTidakBeraturan)
  (sudutSiku 0)
  (sudutLancip 2)
  (sudutTumpul 2)
  (jumlahPasanganSejajar 0)
  =>
  (assert (objek layangLayang)))

(defrule isTrapesium
  (objek segiempatTidakBeraturan)
  (jumlahPasanganSejajar 1)
  =>
  (assert (objek trapesium)))

(defrule isTrapesiumSamaKaki
  (objek trapesium)
  (sepasangSudutSama 2)
  =>
  (assert (objek trapesiumSamaKaki)))

(defrule isTrapesiumRataKanan
  (objek trapesium)
  (maksXSiku true)
  =>
  (assert (objek trapesiumRataKanan)))

(defrule isTrapesiumRataKiri
  (objek trapesium)
  (minXSiku true)
  =>
  (assert (objek trapesiumRataKiri)))

(defrule isSegilimaTidakBeraturan ""
   (sisi 5)
   =>
   (assert (objek segilimaTidakBeraturan)))

(defrule isSegiEnamTidakBeraturan ""
   (sisi 6)
   =>
   (assert (objek segienamTidakBeraturan)))

(defrule isSegiEnamBeraturan
  (objek segienamTidakBeraturan)
  (enamSisiSama true)
  =>
  (assert (objek segiEnamBeraturan)))

(defrule isSegiLimaBeraturan
  (objek segilimaTidakBeraturan)
  (limaSisiSama true)
  =>
  (assert (objek segiLimaBeraturan)))

(defrule isSegitigaLancip
  (objek segitigaTidakBeraturan)
  (sudutLancip 3)
  =>
  (assert (objek segitigaLancip)))

(defrule isSegitigaTumpul
  (objek segitigaTidakBeraturan)
  (sudutTumpul 1)
  =>
  (assert (objek segitigaTumpul)))

(defrule isSegitigaSikuSiku
  (objek segitigaTidakBeraturan)
  (sudutSiku 1)
  =>
  (assert (objek segitigaSiku)))

(defrule isSegitigaSamaKaki
  (objek segitigaTidakBeraturan)
  (jumlahSudutSama 2)
  (jumlahSisiSama 2)
  =>
  (assert (objek segitigaSamaKaki)))

(defrule isSegitigaSamaKakiSikuSiku
  (objek segitigaSamaKaki)
  (sudutSiku 1)
  =>
  (assert (objek segitigaSamaKakiSikuSiku)))

(defrule isSegitigaSamaKakiLancip
  (objek segitigaSamaKaki)
  (sudutLancip 3)
  =>
  (assert (objek segitigaSamaKakiLancip)))

(defrule isSegitigaSamaKakiTumpul
  (objek segitigaSamaKaki)
  (sudutTumpul 1)
  =>
  (assert (objek segitigaSamaKakiTumpul)))

(defrule isSegitigaSamaSisi
  (objek segitigaTidakBeraturan)
  (jumlahSudutSama 3)
  (jumlahSisiSama 3)
  =>
  (assert (objek segitigaSamaKakiTumpul)))
