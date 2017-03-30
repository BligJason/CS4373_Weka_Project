file = fullfile('d:/','datamining','datasets','datasets','dota2Dataset','output.txt');
t = readtable(file);
bar(t.(2));
set(gca,'XTickLabel',t.(1));