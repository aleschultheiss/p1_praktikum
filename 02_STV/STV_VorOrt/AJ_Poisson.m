M1 = dlmread('TV2_50Messungen.stat', ' ', 15, 0);
M2 = dlmread('TV2_100Messungen.stat', ' ', 15, 0);

cnt1 = M1(:, 1);
haeuf1 = M1(:, 2);
cnt2 = M2(:, 1);
haeuf2 = M2(:, 2);
mu1 = (1/sum(haeuf1)) * dot(haeuf1, cnt1)
mu2 = (1/sum(haeuf2)) * dot(haeuf2, cnt2)
o1 = sqrt(1/(sum(haeuf1)-1) * dot(haeuf1, (cnt1-mu1).^2))
o2 = sqrt(1/(sum(haeuf2)-1) * dot(haeuf2, (cnt2-mu2).^2))

[ax, h1, h2] = plotyy(cnt1, haeuf1, cnt2, haeuf2, 'bar', 'bar');

title('Verteilung Haeufigkeit der Counts im Energieintervall');
xlabel('Counts');
ylabel('Haeufigkeit');

hold on

s1 = stem(mu1, 16);
s2 = stem(mu2, 16);
legend([h1, h2, s1, s2], {'50 Messungen', '100 Messungen', 'Mittelwert 50 Messungen', 'Mittelwert 100 Messungen'})
