import java.util.*;

class Solution {

    public int specialNodes(int n, int[][] edges, int x, int y, int z) {

        List<Integer>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int[] e : edges) {
            int u = e[0];
            int v = e[1];

            graph[u].add(v);
            graph[v].add(u);
        }

        int[] dx = bfs(graph, x);
        int[] dy = bfs(graph, y);
        int[] dz = bfs(graph, z);

        int ans = 0;

        for (int i = 0; i < n; i++) {
            long a = dx[i];
            long b = dy[i];
            long c = dz[i];

            long[] arr = {a, b, c};
            Arrays.sort(arr);

            if (arr[0] * arr[0] + arr[1] * arr[1] == arr[2] * arr[2]) {
                ans++;
            }
        }

        return ans;
    }

    private int[] bfs(List<Integer>[] graph, int src) {
        int n = graph.length;

        int[] dist = new int[n];
        Arrays.fill(dist, -1);

        Queue<Integer> q = new LinkedList<>();
        q.offer(src);
        dist[src] = 0;

        while (!q.isEmpty()) {
            int u = q.poll();

            for (int v : graph[u]) {
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    q.offer(v);
                }
            }
        }

        return dist;
    }
}