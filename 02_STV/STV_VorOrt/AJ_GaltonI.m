k = 0:10;
nk = [0, 0, 10, 32, 49, 71, 51, 34, 7, 1, 1];
ng = [2, 27, 126, 309, 543, 602, 491, 308, 133, 24, 8];
muk = 1/sum(nk) * dot(k, nk)
ok = sqrt(1/(sum(nk)-1) * dot(nk, (k-mu).*(k-mu)))
mug = 1/sum(ng) * dot(k, ng)
og = sqrt(1/(sum(ng)-1) * dot(ng, (k-mu).*(k-mu)))

[ax, h1, h2] = plotyy(k, nk, k, ng, 'bar', 'bar');

title('Verteilung des Galton Bretts');
xlabel('Kanal');
ylabel('Anzahl Kugeln');

hold on
s1 = stem(muk, 71);
s2 = stem(mug, 71);

legend([h1, h2, s1, s2], {'Mittlere Statistik: 256 Kugeln', 'Grosse Statistik: 2560 Kugeln', 'Mittelwert der mittleren Statistik', 'Mittelwert der grossen Statistik'})
