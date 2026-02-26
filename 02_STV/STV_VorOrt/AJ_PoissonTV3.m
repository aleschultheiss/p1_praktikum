M1 = dlmread('TV3_100Messungen.stat', ' ', 15, 0)

cnt1 = M1(:, 1);
haeuf1 = M1(:, 2);
mu1 = (1/sum(haeuf1)) * dot(haeuf1, cnt1)
o1 = sqrt(1/(sum(haeuf1)-1) * dot(haeuf1, (cnt1-mu1).^2))

h1 = bar(cnt1, haeuf1/sum(haeuf1))

title('Verteilung Haeufigkeit der Counts im groﬂen Energieintervall');
xlabel('Counts');
ylabel('Relative Haeufigkeit');

hold on

h2 = plot(cnt1, normpdf(cnt1, mu1, o1))

legend([h1, h2], {'Gemessene Verteilung','Normalverteilung'})
