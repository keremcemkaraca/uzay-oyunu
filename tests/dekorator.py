import pytest
from uzay_oyunu.dekoratorler import sure_olc, say, log_cagri, sinirla, hafiza
from uzay_oyunu.komutlar import KOMUTLAR, komut


def test_sure_olc():
    @sure_olc
    def topla(a, b=0):
        """Toplama islemi."""
        return a + b

    assert topla(3, b=5) == 8
    assert topla.__name__ == "topla"
    assert topla.__doc__ == "Toplama islemi."

    def test_say():
        @say
        def islem():
            pass

        islem()
        islem()
        assert islem.cagri == 2

        def test_log_cagri(capsys):
            @log_cagri
            def carp(a, b):
                return a * b

            carp(2, b=3)
            captured = capsys.readouterr()
            assert "-> carp(2, b=3)" in captured.out
            assert "<<- carp 6" in captured.out

            def test_komutlar():
                assert "yardim" in KOMUTLAR
                assert "envanter" in KOMUTLAR
                assert "harita" in KOMUTLAR

                with pytest.raises(ValueError):
                    @komut("yardim")
                    def sahte_yardim(durum):
                        pass