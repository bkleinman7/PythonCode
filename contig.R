patterns <- readLines("input.txt");
k <- nchar(patterns[1]);
vx.start <- substring(patterns,1,k-1);
vx.end <- substring(patterns,2,k);
paths <- paste(vx.start,vx.end, sep=" -> ");
graph.desc <- strsplit(paths," -> ");
g.adj <- t(matrix(unlist(sapply(graph.desc, function(x){
  rbind(x[1],unlist(strsplit(x[2],",")));
})), nrow=2));
g.nodes <- data.frame(row.names=unique(c(g.adj)));
g.nodes$e.in <-
  table(factor(g.adj[,2], levels=rownames(g.nodes)))[rownames(g.nodes)];
g.nodes$e.out <-
  table(factor(g.adj[,1], levels=rownames(g.nodes)))[rownames(g.nodes)];
g.nodes$unique <- ((g.nodes$e.in * g.nodes$e.out) == 1);
contigs <- NULL;
startPos <- 1;
while((startPos <= nrow(g.adj)) &&
      (g.nodes[g.adj[startPos,1],"unique"] == 1)){
  startPos <- startPos+1;
}
path <- g.adj[startPos,];
while(startPos <= nrow(g.adj)){
  if(g.nodes[tail(path,1),"unique"]){
    nextRow <- match(tail(path,1),g.adj[,1]);
    newNode <- g.adj[nextRow,2];
    path <- c(path,newNode);
  } else { ## spit out contig, move to next contig start
    contigs <- c(contigs,paste0(paste(substring(head(path,-1),1,1),
                                      collapse=""),
                                tail(path,1)));
    startPos <- startPos+1;
    while((startPos <= nrow(g.adj)) &&
          (g.nodes[g.adj[startPos,1],"unique"] == 1)){
      startPos <- startPos+1;
    }
    path <- if(startPos <= nrow(g.adj)){
      g.adj[startPos,];
    } else { NULL }
  }
}
if(length(path) > 1){
  contigs <- c(contigs,paste0(paste(substring(head(path,-1),1,1),
                                    collapse=""),
                              tail(path,1)));
}
print(contigs)
#cat(sort(contigs),sep="\n");
#cat(sort(contigs),sep="\n", file="output.txt")